import pytest

from client.api import Pet
from src.body_samples.pet import body_pet


@pytest.fixture
def create_new_pet():
    response = Pet().add(body=body_pet)
    return response.json()['id']
