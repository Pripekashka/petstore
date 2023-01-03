from client.api import Pet


def get_pet_by_id(id_pet: int):
    """
    Получить информацию по id карточки
    """
    return Pet().find_by_id(petid=id_pet)
