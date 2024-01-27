from abc import ABC, abstractmethod

import requests

from api.exceptions import HeadHunterAPIAvailableError, HeadHunterRequestAPIError
from config import HH_URL


class Api(ABC):

    @abstractmethod
    def get_response(self) -> list[dict]:
        pass


class HeadHunterAPI(Api):

    def __init__(self, search_query: str, top_n, filter_words):
        self.search_query = search_query
        self.top_n = top_n
        self.filter_words = filter_words

    def get_response(self) -> list[dict]:
        params = {
            'per_page': self.top_n,
            'text': self.search_query,
            'search_field': 'name',
            'salary': 0
        }
        response = requests.get(HH_URL, params=params)
        if response.status_code == 200:
            data = response.json()
        if response.status_code == 500:
            raise HeadHunterAPIAvailableError('HH не доступен')
        if response.status_code in (400, 403, 404):
            errors: list[dict] = response.json()['errors']
            raise HeadHunterRequestAPIError(f'Ошибка данных запроса {errors}')

        return data['items']
