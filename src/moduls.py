from abc import ABC, abstractmethod
from pprint import pprint

import requests
import json


class Api(ABC):

    @abstractmethod
    def get_vacancies(self):
        pass


class HeadHunterAPI(Api):

    @staticmethod
    def get_vacancies(search_parameter: str = 'python'):
        url = 'https://api.hh.ru/vacancies'
        params = {
            'per_page': 100,
            'text': search_parameter,
            'search_field': 'name',
        }
        response = requests.get(url=url, params=params)
        data = response.json()
        with open('../data/data_vacancies.json', 'w', encoding='utf-8') as f:
            json.dump(data['items'], f, ensure_ascii=False, indent=4)
            f.close()
        return data['items']


class Vacancy:

    def __init__(self, name: str, salary: list, alternate_url: str, responsibility: str, schedule: str):
        self.name = name
        self.salary = salary
        self.alternate_url = alternate_url
        self.responsibility = responsibility
        self.schedule = schedule


    @classmethod
    def initialization(cls, data: list):
        vacancy_list = []
        for item in data:
            vacancy = cls(
                name=item['name'],
                salary=item['salary'],
                alternate_url=item['alternate_url'],
                responsibility=item['snippet']['responsibility'],
                schedule=item['schedule']['name']
            )
            vacancy_list.append(vacancy)
        return vacancy_list


class JSONSaver:
    def __init__(self):
        pass


if __name__ == '__main__':
    api = HeadHunterAPI()
    vacancy = Vacancy.initialization(api.get_vacancies('Python'))
    for item in vacancy:
        print(item.name)
        print(item.salary)
        print(item.alternate_url)
        print(item.responsibility)
        print(item.schedule)
        print('____________________________')