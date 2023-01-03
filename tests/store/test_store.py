import pytest
from datetime import datetime

from client.api import Store
from src.body_samples.store import body_store
from src.helpers.pet import get_pet_by_id
from src.data.assertion_errors import PET_NOT_PLACED


@pytest.mark.xfail(reason='Status not changed. https://jira.../DEV-123')
def test_create_order(create_new_pet):
    """
    Создание заказа
    """
    shipdate = str(datetime.now()).replace(' ', 'T') + 'Z'
    body_store['petId'] = create_new_pet
    body_store['shipDate'] = shipdate
    Store().create_order(body=body_store)
    new_status = get_pet_by_id(id_pet=create_new_pet).json()['status']
    assert new_status == 'placed', f'{PET_NOT_PLACED}{new_status}'
