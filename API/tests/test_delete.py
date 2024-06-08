import allure
import pytest
from assertpy import assert_that
from API.src.constants.urls import BASE_PET_URL
from API.src.enums.common import HttpStatusCode


class TestUserDeleteRequests:
    @allure.feature("DELETE")
    @allure.title("Delete a pet")
    @allure.id("1")
    @pytest.mark.smoke
    def test_delete_pet(self, delete_api, create_pet, get_api):
        url = f'{BASE_PET_URL}/{create_pet["id"]}'
        headers = delete_api.get_headers()

        deleted_pet_response = delete_api.request(url, headers)

        assert_that(deleted_pet_response["status_code"]).is_equal_to(HttpStatusCode.OK.value)
        assert_that(deleted_pet_response["response"]["message"]).is_equal_to(str(create_pet["id"]))

        url = f'{BASE_PET_URL}/{create_pet["id"]}'
        headers = get_api.get_headers()

        get_pet_response = get_api.request(url, headers)

        assert_that(get_pet_response["status_code"]).is_equal_to(HttpStatusCode.NotFound.value)
