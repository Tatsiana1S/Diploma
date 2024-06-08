from API.src.constants.urls import BASE_PET_URL


def upload_image_link_generator(pet_id: int) -> str:
    """
    This function generates upload image link (url)
    :param pet_id: pet id
    :return: link
    """
    return f'{BASE_PET_URL}/{pet_id}/uploadImage'
