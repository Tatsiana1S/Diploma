import pytest
from API.src.api.delete_api import DeleteApi
from API.src.api.get_api import GetApi
from API.src.api.post_api import PostApi
from API.src.api.put_api import PutApi
from API.src.constants.urls import BASE_PET_URL
from API.src.mock_data.pet import create_pet_payload


@pytest.fixture
def create_pet(post_api, delete_api):
    url = BASE_PET_URL
    headers = post_api.get_headers()
    data = create_pet_payload.model_dump_json()

    added_pet_response = post_api.request(url, headers, data)

    yield added_pet_response["response"]

    try:
        url = f'{BASE_PET_URL}/{added_pet_response["response"]["id"]}'
        headers = delete_api.get_headers()

        delete_api.request(url, headers)

    except Exception:
        print("Pet already deleted")


@pytest.fixture()
def get_api():
    return GetApi()


@pytest.fixture()
def post_api():
    return PostApi()


@pytest.fixture()
def put_api():
    return PutApi()


@pytest.fixture()
def delete_api():
    return DeleteApi()
