import requests


class Client:
    @staticmethod
    def request_and_validate(method: str, url: str, status_code: int = 200,
                             **kwargs) -> requests.Response:
        """
        Do request and validate status code

        method: type method for request. GET, OPTIONS, HEAD, POST, PUT, PATCH, or DELETE
        url: url for request
        status_code: waiting status code in response. Default = 200
        """
        response = requests.request(method, url, **kwargs)
        assert response.status_code == status_code, \
            f'Invalid status code. Wait: {status_code}, get: {response.status_code}, ' \
            f'{response.text}'
        return response
