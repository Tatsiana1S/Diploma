import requests
from typing import Dict
from API.src.api.base_api import BaseApi


class GetApi(BaseApi):
    def request(self, url: str, headers: Dict[str, str], params: Dict[str, str] = {}) -> Dict:
        """
        This method makes request by url
        :param url: url
        :param headers: headers
        :return: transformed response
        """
        response = requests.get(
            url=url,
            headers=headers,
            params=params
        )

        return self.transform_response(response)

    @staticmethod
    def get_headers() -> Dict[str, str]:
        """
        This method returns headers
        :return: headers
        """
        return {
            "accept": "application/json"
        }
