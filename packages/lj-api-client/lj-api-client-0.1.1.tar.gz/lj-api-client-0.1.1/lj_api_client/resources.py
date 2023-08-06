import json

from lj_api_client.utils import urljoin

class ResourcePool:
    def __init__(self, endpoint, session):
        self._endpoint = endpoint
        self._session = session

    def get_url(self):
        return self._endpoint

class CreatableResource:
    def create_item(self, item, params=None):
        res = self._session.post(self._endpoint, data=json.dumps(item), params=params)
        return res

class GettableResource:
    def fetch_item(self, code, params=None):
        url = urljoin(self._endpoint, code)
        res = self._session.get(url, params=params)
        return res

class ListableResource:
    def fetch_list(self, params=None):
        res = self._session.get(self._endpoint, params=params)
        return res

class UpdatableResource:
    def update_item(self, code, item, params=None):
        url = urljoin(self._endpoint, code)
        res = self._session.patch(url, data=json.dumps(item), params=params)
        return res

class DeletableResource:
    def delete_item(self, code, params=None):
        url = urljoin(self._endpoint, code)
        res = self._session.delete(url, params=params)
        return res

# Pools

# Users Pool
class UsersPool(ResourcePool, ListableResource):
    pass

# Workspaces Pool
class WorkspacesPool(ResourcePool, ListableResource, GettableResource):
    
    def cards(self, workspace_id):
        return CardsPool(
            urljoin(self._endpoint, workspace_id, 'cards'), self._session
        )

# Cards Pool
class CardsPool(
    ResourcePool, 
    ListableResource, 
    GettableResource, 
    CreatableResource, 
    UpdatableResource, 
    DeletableResource):

    def presigned_url(self, card_id):
        return CardsPresignedUrlPool(
            urljoin(self._endpoint, card_id, 'presigned-url'), self._session
        )

    def feed(self, card_id):
        return CardsFeedPool(
            urljoin(self._endpoint, card_id, 'feed'), self._session
        )

class CardsPresignedUrlPool(
    ResourcePool,
    ListableResource):
    pass

class CardsFeedPool(
    ResourcePool,
    CreatableResource):
    pass