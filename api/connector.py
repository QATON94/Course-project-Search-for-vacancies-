from abc import ABC, abstractmethod

import requests

from api.exceptions import HeadHunterAPIAvailableError, HeadHunterRequestAPIError
from config import HH_URL


class Api(ABC):
    """
    Абстрактный класс для API
    """

    @abstractmethod
    def get_response(self) -> list[dict]:
        pass


class HeadHunterAPI(Api):
    """
    Класс API для HeadHunter
    """

    def __init__(self, search_query: str):
        self.search_query = search_query


    def get_response(self) -> list[dict]:
        """
        Возвращает ответ от HeadHunter
        """
        params = {
            'per_page': 100,
            'text': self.search_query,
            'search_field': 'name',
            'currency': "RUR",
            'only_with_salary': True,
            'area': 113
        }
        response = requests.get(HH_URL, params=params)
        data = []
        if response.status_code == 200:
            data: list[dict] = response.json()
        if response.status_code == 500:
            raise HeadHunterAPIAvailableError('HH не доступен')
        if response.status_code in (400, 403, 404):
            errors: list[dict] = response.json()['errors']
            raise HeadHunterRequestAPIError(f'Ошибка данных запроса {errors}')
        return data
