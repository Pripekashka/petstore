import pytest

from client.api import Pet
from src.body_samples.pet import body_pet
from src.data.assertion_errors import INCORRECT_PET_ID, INCORRECT_NAME_PET, PET_NOT_FOUND
from src.helpers.pet import get_pet_by_id


@pytest.mark.parametrize('id_pet', (-1, 0, 1, 999999))
def test_add_new_pet_valid(id_pet):
    """
    Успешное создание карточки, при разных валидных значениях id
    """
    body_pet['id'] = id_pet
    response = Pet().add(body=body_pet)
    if id_pet > 0:
        assert response.json()['id'] == id_pet, INCORRECT_PET_ID


@pytest.mark.parametrize('id_pet', ('a', {'123': '123'}))
def test_add_new_pet_invalid(id_pet):
    """
    Неуспешное создание карточки, при разных невалидных значениях id
    """
    body_pet['id'] = id_pet
    Pet().add(body=body_pet, status_code=500)


def test_update_pet(create_new_pet):
    """
    Обновление имени карточки
    """
    new_name = 'kekw'
    body_pet['id'] = create_new_pet
    body_pet['name'] = new_name
    Pet().update(body=body_pet)
    name = get_pet_by_id(create_new_pet).json()['name']
    assert name == new_name, INCORRECT_NAME_PET


def test_delete_by_id_pet(create_new_pet):
    """
    Удаление записи и проверка ее отсутствия
    """
    Pet().delete_by_id(petid=create_new_pet)
    response = Pet().find_by_id(petid=create_new_pet, status_code=404)
    assert response.json()['message'] == PET_NOT_FOUND

