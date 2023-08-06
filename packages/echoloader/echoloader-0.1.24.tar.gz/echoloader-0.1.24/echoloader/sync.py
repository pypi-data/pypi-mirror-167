import datetime
import io
import logging
import threading
import time

import requests
from dateutil import parser
from pydicom import dcmread
from pynetdicom import AE

from echoloader.lib import unpack

logger = logging.getLogger('echolog')
DEFAULT_AE_TITLE = "Us2.ai"


class PacsConnection:
    def __init__(self, details):
        parts = details.split(':')
        self.host, port, self.remote_ae_title = parts[:3]
        self.local_ae_title = parts[3] if len(parts) > 3 else DEFAULT_AE_TITLE
        self.port = int(port)

    def store(self, ds):
        ae = AE(ae_title=self.local_ae_title)
        ae.add_requested_context(ds.SOPClassUID, ds.file_meta.TransferSyntaxUID)
        assoc = ae.associate(self.host, self.port, ae_title=self.remote_ae_title)
        if not assoc.is_established:
            raise ConnectionError('Association rejected, aborted or never connected')
        # Use the C-STORE service to send the dataset
        # returns the response status as a pydicom Dataset
        try:
            # force treat context as supporting the SCP role
            for cx in assoc.accepted_contexts:
                cx._as_scp = True

            status = assoc.send_c_store(ds)

            # Check the status of the storage request
            if status:
                # If the storage request succeeded this will be 0x0000
                logger.debug(f'C-STORE request status: 0x{status.Status:04x}')
            else:
                raise ValueError('Connection timed out, was aborted or received invalid response')
        finally:
            # Release the association
            assoc.release()

    def __str__(self):
        return f"{self.host}:{self.port}"


class Sync(threading.Thread):
    def __init__(self, cmd, *vargs, **kwargs):
        super().__init__(*vargs, **kwargs)
        self.args = cmd
        self.connections = cmd.sync
        self.auth = cmd.auth
        self.api_url = self.auth.api_url
        self.customer = cmd.customer
        self.killed = False
        self.search = f"{self.api_url}/study/search?customer={self.customer}&reportCompleted=true"
        self.last_sync = datetime.datetime.min.replace(tzinfo=datetime.timezone.utc)
        self.params = {}
        if cmd.sync_url:
            self.params['url'] = True
        if cmd.sync_main_findings:
            self.params['main_findings'] = True

    def sr(self, sid):
        return f"{self.api_url}/study/sr/{sid}"

    def latest_mod(self, sid):
        return unpack(requests.get(
            f"{self.api_url}/sync/modification/{sid}", params={'limit': 1}, headers=self.auth.get_headers()))[0]

    def stop(self):
        self.killed = True

    def sync(self):
        t = self.last_sync
        res = unpack(requests.get(self.search, headers=self.auth.get_headers()), {})
        results = res.get('results', [])
        for study in results:
            sid = study['id']
            try:
                mod = self.latest_mod(sid)
                creation = parser.parse(mod['creation']).replace(tzinfo=datetime.timezone.utc)
                if creation > self.last_sync:
                    bs = unpack(requests.get(self.sr(sid), headers=self.auth.get_headers(), params=self.params))
                    ds = dcmread(io.BytesIO(bs))
                    for conn in self.connections:
                        conn.store(ds)
                        logger.info(f'Synced {sid} to {conn}')
                t = max(creation, t)
            except Exception as exc:
                logger.error(f'Failed to sync SR for {sid} due to {exc}')
        self.last_sync = t

    def run(self) -> None:
        while not self.killed:
            try:
                self.sync()
            except Exception as exc:
                logger.error(f'Failed sync due to: {exc}')
            time.sleep(10)
