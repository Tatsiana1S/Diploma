import os
import pathlib

import allure
import pytest
from assertpy import assert_that
from API.src.enums.common import HttpStatusCode
from API.src.helpers.link_generator import upload_image_link_generator
from API.src.mock_data.pet import create_pet_payload
from API.src.constants.urls import BASE_PET_URL
from API.src.models.pet_model import PetModel


class TestUserPostRequests:
    @allure.feature("POST")
    @allure.title("Create a pet")
    @allure.id("1")
    @pytest.mark.smoke
    def test_create_pet(self, post_api, get_api, delete_api):
        pet_id = create_pet_payload.id
        expected_pet = create_pet_payload.model_dump()

        try:
            url = BASE_PET_URL
            headers = post_api.get_headers()
            data = create_pet_payload.model_dump_json()

            added_pet_response = post_api.request(url, headers, data)

            test = PetModel(**added_pet_response["response"])
            print(test.id)

            assert_that(added_pet_response["status_code"]).is_equal_to(HttpStatusCode.OK.value)
            assert_that(added_pet_response["response"]).is_equal_to(expected_pet)

            url = f'{BASE_PET_URL}/{pet_id}'
            headers = get_api.get_headers()

            get_pet_response = get_api.request(url, headers)

            assert_that(get_pet_response["status_code"]).is_equal_to(HttpStatusCode.OK.value)
            assert_that(get_pet_response["response"]).is_equal_to(expected_pet)

        finally:
            url = f'{BASE_PET_URL}/{pet_id}'
            headers = delete_api.get_headers()

            delete_api.request(url, headers)

    @allure.feature("POST")
    @allure.title("Update a pet in the store with form data")
    @allure.id("1")
    @pytest.mark.regression
    def test_update_pet_form_data(self, create_pet, get_api, post_api):
        url = f'{BASE_PET_URL}/{create_pet["id"]}'
        headers = get_api.get_headers()
        data = {
            "name": "Test2",
            "status": "sold"
        }

        added_pet_response = post_api.request(url, headers, data)

        assert_that(added_pet_response["status_code"]).is_equal_to(HttpStatusCode.OK.value)
        assert_that(added_pet_response["response"]["message"]).is_equal_to(str(create_pet["id"]))

        url = f'{BASE_PET_URL}/{create_pet["id"]}'
        headers = get_api.get_headers()

        get_pet_response = get_api.request(url, headers)

        assert_that(get_pet_response["status_code"]).is_equal_to(HttpStatusCode.OK.value)
        assert_that(get_pet_response["response"]["name"]).is_equal_to(data["name"])
        assert_that(get_pet_response["response"]["status"]).is_equal_to(data["status"])

    @allure.feature("POST")
    @allure.title("Upload an image")
    @allure.id("1")
    @pytest.mark.regression
    def test_upload_image(self, create_pet, get_api, post_api):
        url = upload_image_link_generator(create_pet["id"])
        headers = get_api.get_headers()
        data = {"additionalMetadata": "Download image"}

        file_path = os.path.join(os.path.dirname(__file__), '../src/files/pet_image.png')

        files = {"file": open(file_path, "rb")}

        upload_image_response = post_api.request(url, headers, data, files)

        assert_that(upload_image_response["status_code"]).is_equal_to(HttpStatusCode.OK.value)
