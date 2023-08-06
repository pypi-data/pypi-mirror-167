from typing import List

import requests as rq
from pydantic import validate_arguments

from lj_api_client import utils, resources, schemas, exceptions


class Client:
    DEFAULT_HOST = "https://public-api.livejourney.io"

    def __init__(self, api_key, host=None, api_version='v1'):
        if not host:
            host = self.DEFAULT_HOST

        self._base_url = utils.urljoin(host, 'api', api_version)
        self._session = rq.Session()
        self._session.headers.update({
            'x-api-key': api_key,
            'content-type': 'application/json'
        })

        self._resources = {
            'users': resources.UsersPool(
                utils.urljoin(self._base_url, 'users'), self._session
            ),
            'workspaces': resources.WorkspacesPool(
                utils.urljoin(self._base_url, 'workspaces'), self._session
            ),
        }

    @property
    def resources(self):
        return self._resources

    @property
    def users(self):
        return self.resources.get('users')

    @property
    def workspaces(self):
        return self.resources.get('workspaces')

    def get_user(self) -> rq.Response:
        return self.users.fetch_list()

    def get_workspaces(self) -> rq.Request:
        return self.workspaces.fetch_list()

    def get_workspace(self, workspace_id: str) -> rq.Response:
        return self.workspaces.fetch_item(workspace_id)

    def get_cards(self, workspace_id: str) -> rq.Response:
        return self.workspaces.cards(workspace_id).fetch_list()

    def get_card(self, workspace_id: str, card_id: str) -> rq.Response:
        return self.workspaces.cards(workspace_id).fetch_item(card_id)

    @validate_arguments
    def create_card(self, workspace_id: str, card_data: schemas.CardCreationModel) -> rq.Request:
        return self.workspaces.cards(workspace_id).create_item(card_data.dict(exclude_none=True))

    @validate_arguments
    def update_card(self, workspace_id: str, card_id: str, card_data: schemas.CardUpdateModel) -> rq.Request:
        return self.workspaces.cards(workspace_id).update_item(card_id, card_data.dict(exclude_none=True))

    def delete_card(self, workspace_id: str, card_id: str) -> rq.Response:
        return self.workspaces.cards(workspace_id).delete_item(card_id)

    def upload_data_to_card(self, workspace_id: str, card_id: str, log_file_path: str, desc_file_path: str = None):
        res = self.get_card(workspace_id, card_id)
        if res.status_code != 200:
            exceptions.raise_request_exception_from_res(res)

        last_import_status = res.json()['data']['card']['last_import_status']
        if last_import_status not in ['EMPTY', 'DONE', 'ERROR']:
            raise exceptions.CardNotReadyError('Previous data import in progress, please retry later')
        elif last_import_status == 'ERROR':
            raise exceptions.CardError('An error occurred on your card please contact support or create new card')

        files_data = [
            file_data 
            for file_data in [(log_file_path, 'log'), (desc_file_path, 'descriptive')]
            if file_data[0]
        ]
        for file_path, _ in files_data:
            utils.validate_file_path(file_path)

        for file_path, data_type in files_data:
            res = self.workspaces.cards(workspace_id).presigned_url(card_id).fetch_list(params={'data_type': data_type})
            if res.status_code != 200:
                exceptions.raise_request_exception_from_res(res)

            presigned_url = res.json()['data']['presigned_url']
            with open(file_path, 'rb') as f:
                res = rq.post(presigned_url['url'], files={'file': f}, data=presigned_url['fields'])
            if res.status_code != 204:
                exceptions.raise_request_exception_from_res(res)

        res = self.workspaces.cards(workspace_id).feed(card_id).create_item({})
        if res.status_code != 201:
            exceptions.raise_request_exception_from_res(res)
        
        return res
        
