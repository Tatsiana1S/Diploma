import allure
import pytest
from assertpy import assert_that
from API.src.constants.urls import BASE_PET_URL
from API.src.enums.common import HttpStatusCode
from API.src.mock_data.pet import update_pet_payload


class TestUserPutRequests:
    @allure.feature("PUT")
    @allure.title("Update an existing pet")
    @allure.id("1")
    @pytest.mark.smoke
    def test_update_pet(self, create_pet, get_api, put_api):
        pet_id = update_pet_payload.id
        expected_pet = update_pet_payload.model_dump()

        url = f'{BASE_PET_URL}'
        headers = put_api.get_headers()
        data = update_pet_payload.model_dump_json()

        put_pet_response = put_api.request(url, headers, data)

        assert_that(put_pet_response["status_code"]).is_equal_to(HttpStatusCode.OK.value)
        assert_that(put_pet_response["response"]).is_equal_to(expected_pet)

        url = f'{BASE_PET_URL}/{pet_id}'
        headers = get_api.get_headers()

        get_pet_response = get_api.request(url, headers)

        assert_that(get_pet_response["status_code"]).is_equal_to(HttpStatusCode.OK.value)
        assert_that(get_pet_response["response"]).is_equal_to(expected_pet)
