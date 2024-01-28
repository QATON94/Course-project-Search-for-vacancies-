from abc import ABC, abstractmethod


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