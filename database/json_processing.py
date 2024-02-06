import json
from abc import ABC, abstractmethod
from typing import Any

from vecancy_worcer.vecancy import Vacancy


class FileProcessing(ABC):

    @abstractmethod
    def __init__(self, path: str) -> None:
        pass

    @abstractmethod
    def read(self) -> list:
        pass

    @abstractmethod
    def write(self, data: list[dict]) -> None:
        pass

    @abstractmethod
    def get(self, query: str) -> list[dict]:
        pass

    @abstractmethod
    def delete(self, query: str) -> None:
        pass


class JsonProcessing(FileProcessing):

    def __init__(self, path: str) -> None:
        """
        :param path: Путь к файлу
        """
        self.path = path

    def read(self) -> list[dict]:
        """
        Открытие фала на чтение
        :return: Список с вакансиями
        """
        with open(self.path, encoding='utf-8') as f:
            return json.load(f)

    def write(self, data: list | Vacancy) -> None:
        """
        Открытие фала на запись
        :param data: Список с вакансиями
        """
        json_vacancy = []
        if type(data) is list:
            for item in data:
                json_vacancy.append(item.__dict__)
        else:
            json_vacancy.append(data.__dict__)
        with open(self.path, "w", encoding='utf-8') as f:
            json.dump(json_vacancy, f, ensure_ascii=False, indent=4)

    def get(self, query: list) -> list[dict]:
        """
        Поиск вакансий по запросу
        :param query: Слово запроса
        :return: Список с вакансиями
        """
        get_query = []
        with open(self.path, encoding='utf-8') as f:
            data = json.load(f)
        for item in data:
            for word in query:
                if word.lower() in str(item.values()).lower():
                    get_query.append(item)
                    break

        return get_query

    def delete(self, query: str) -> None:
        """
        Удаление вакансий по запросу
        :param query: Слово запроса
        """
        with open(self.path, encoding='utf-8') as f:
            data = json.load(f)
            items: int = 0
            check: int = len(data)
            while check != items:
                check = items
                for item in data:
                    for word in item.values():
                        if query.lower() in str(word).lower():
                            data.remove(item)
                            break
                items = len(data)
        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
