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

    def add_vacancy(self, vacancy:list):
        json_vacansy = []
        for item in vacancy:
            json_vacansy.append(item.__dict__)
        with open('../data/data_vacancies.json', 'w', encoding='utf-8') as f:
            json.dump(json_vacansy, f, ensure_ascii=False, indent=4)
            f.close()

    def get_vacancies_by_salary(self, query_word):
        with open('../data/data_vacancies.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        for item in data:
            if query_word in item['salary']:
                pprint(item)


if __name__ == '__main__':
    hh_api = HeadHunterAPI()

    hh_vacancies = hh_api.get_vacancies("Python")

    # for item in hh_vacancies:
    #     print(item.name)
    #     print(item.salary)
    #     print(item.alternate_url)
    #     print(item.responsibility)
    #     print(item.schedule)
    #     print('____________________________')
    vacancy = Vacancy.initialization(hh_vacancies)
    json_saver = JSONSaver()
    json_saver.add_vacancy(vacancy)
    # json_saver.get_vacancies_by_salary("100 000-150 000 руб.")