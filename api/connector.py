from abc import ABC, abstractmethod

import requests

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
        data: list[dict] = response.json()
        return data
