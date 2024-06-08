import pytest
from assertpy import assert_that
from API.src.constants.urls import BASE_PET_URL, GET_PETS_BY_STATUS
import allure
from API.src.enums.common import HttpStatusCode


class TestUserGetRequests:
    @allure.feature("GET")
    @allure.title("Get pets by status")
    @allure.id("1")
    @pytest.mark.regression
    @pytest.mark.parametrize("statuses", [
        pytest.param(["available"]),
        pytest.param(["pending"]),
        pytest.param(["sold"]),
        pytest.param(["available", "pending"]),
        pytest.param(["pending", "sold"]),
        pytest.param(["available", "sold"]),
        pytest.param(["available", "pending", "sold"])
    ])
    def test_get_pets_by_status(self, statuses, get_api):
        url = GET_PETS_BY_STATUS
        headers = get_api.get_headers()
        params = {"status": ",".join(statuses)}

        get_pet_response = get_api.request(url, headers, params)

        invalid_pets = []
        for pet in get_pet_response["response"]:
            if pet["status"] not in statuses:
                invalid_pets.append(pet)
                break

        assert_that(get_pet_response["status_code"]).is_equal_to(HttpStatusCode.OK.value)
        assert_that(invalid_pets).is_empty()

    @allure.feature("GET")
    @allure.title("Get pets without status")
    @allure.id("1")
    @pytest.mark.regression
    def test_get_pets_without_status(self, get_api):
        url = GET_PETS_BY_STATUS
        headers = get_api.get_headers()

        get_pet_response = get_api.request(url, headers)

        assert_that(get_pet_response["status_code"]).is_equal_to(HttpStatusCode.OK.value)
        assert_that(get_pet_response["response"]).is_empty()

    @allure.feature("GET")
    @allure.title("Get pet by id")
    @allure.id("1")
    @pytest.mark.smoke
    def test_get_pet_by_id(self, create_pet, get_api):
        url = f'{BASE_PET_URL}/{create_pet["id"]}'
        headers = get_api.get_headers()

        get_pet_response = get_api.request(url, headers)

        assert_that(get_pet_response["status_code"]).is_equal_to(HttpStatusCode.OK.value)
        assert_that(get_pet_response["response"]).is_equal_to(create_pet)
