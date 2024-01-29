import json
from abc import ABC, abstractmethod
from pprint import pprint


class FileProcessing(ABC):

    @abstractmethod
    def __init__(self, path):
        pass

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data: list[dict]):
        pass

    @abstractmethod
    def get(self, query: str) -> list[dict]:
        pass

    @abstractmethod
    def delete(self, query: str):
        pass


class JsonProcessing(FileProcessing):

    def __init__(self, path: str):
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

    def write(self, data: list[dict]):
        """
        Открытие фала на запись
        :param data: Список с вакансиями
        """
        json_vacancy = []
        for item in data:
            json_vacancy.append(item.__dict__)
        with open(self.path, "w", encoding='utf-8') as f:
            json.dump(json_vacancy, f, ensure_ascii=False, indent=4)

    def get(self, query: str) -> list[dict]:
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

    def delete(self, query: str):
        """
        Удаление вакансий по запросу
        :param query: Слово запроса
        """
        with open(self.path, encoding='utf-8') as f:
            data = json.load(f)
            items: int = 0
            check:int = len(data)
            while check != items:
                check = items
                for item in data:
                    for word in item.values():
                        if query.lower() in str(word).lower():
                            data.remove(item)
                            break
                items = len(data)
        with open('data/data_vacanciesss.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
