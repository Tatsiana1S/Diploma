import requests
from typing import Dict
from API.src.api.base_api import BaseApi


class PutApi(BaseApi):
    def request(self, url: str, headers: Dict[str, str], data: Dict[str, str]) -> Dict:
        """
        This method makes request by url
        :param url: url
        :param headers: headers
        :return: transformed response
        """
        response = requests.put(
            url=url,
            headers=headers,
            data=data
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
            "Content-Type": "application/json"
        }
