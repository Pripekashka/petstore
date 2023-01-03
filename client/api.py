from client.requests import Client
from src.data.connections import URL


class Pet:
    def __init__(self):
        self.url = URL
        self.client = Client()

    PET_ADD_UPDATE = '/pet'
    PET_FIND_UPDATE_DELETE_BY_ID = '/pet/'

    def add(self, body: dict, status_code: int = 200):
        """
        Add a new pet to the store
        """
        return self.client.request_and_validate(
            "POST", url=f"{self.url}{self.PET_ADD_UPDATE}", json=body,
            status_code=status_code)

    def update(self, body: dict, status_code: int = 200):
        """
        Update an existing pet
        """
        return self.client.request_and_validate(
            "PUT", url=f"{self.url}{self.PET_ADD_UPDATE}", json=body,
            status_code=status_code)

    def find_by_id(self, petid: int, status_code: int = 200):
        """
        Find pet by ID
        """
        return self.client.request_and_validate(
            "GET", url=f"{self.url}{self.PET_FIND_UPDATE_DELETE_BY_ID}{petid}",
            status_code=status_code)

    def delete_by_id(self, petid: int, status_code: int = 200):
        """
        Delete pet by ID
        """
        return self.client.request_and_validate(
            "DELETE", url=f"{self.url}{self.PET_FIND_UPDATE_DELETE_BY_ID}{petid}",
            status_code=status_code)


class Store:
    def __init__(self):
        self.url = URL
        self.client = Client()

    STORE_POST_ORDER = '/store/order'

    def create_order(self, body: dict, status_code: int = 200):
        """
        Place an order for a pet
        """
        return self.client.request_and_validate(
            "POST", url=f"{self.url}{self.STORE_POST_ORDER}", json=body,
            status_code=status_code)
