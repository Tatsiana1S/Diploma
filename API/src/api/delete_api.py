import requests
from typing import Dict
from API.src.api.base_api import BaseApi

API_KEY = "123"


class DeleteApi(BaseApi):
    def request(self, url: str, headers: Dict[str, str]) -> Dict:
        """
        This method makes request by url
        :param url: url
        :param headers: headers
        :return: transformed response
        """
        response = requests.delete(
            url=url,
            headers=headers
        )

        return self.transform_response(response)

    @staticmethod
    def get_headers() -> Dict[str, str]:
        """
        This method returns headers
        :return: headers
        """
        return {
            "accept": "application/json",
            "api_key": f'{API_KEY}'
        }
