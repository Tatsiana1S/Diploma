from typing import Dict


class BaseApi:
    @staticmethod
    def transform_response(response) -> Dict:
        """
        This method transforms response
        :param response: response
        :return: transformed response
        """
        return {
            "response": response.json(),
            "status_code": response.status_code,
        }
