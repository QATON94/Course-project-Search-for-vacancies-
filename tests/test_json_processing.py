import os

import pytest

from database.json_processing import JsonProcessing
from vecancy_worcer.vecancy import Vacancy


@pytest.fixture
def path():
    return os.path.join(os.path.dirname(__file__), 'test_json.json')


@pytest.fixture
def vacancy():
    return Vacancy("Senior Python разработчик", 370000, 300000,
                   "https://hh.ru/vacancy/92135217", "Portal Bilet - e-commerce платформа, "
                                                     "которая занимается продажей билетов и покрывает все сферы event-"
                                                     "сегмента, от небольшого локального события до...",
                   "Удаленная работа")


@pytest.fixture
def vacancy_2():
    vacancy1 = Vacancy("Senior Python разработчик", 370000, 300000,
                       "https://hh.ru/vacancy/92135217", "Portal Bilet - e-commerce платформа, "
                                                         "которая занимается продажей билетов и покрывает все сферы "
                                                         "event-сегмента, от небольшого локального события до...",
                       "Удаленная работа")

    vacancy2 = Vacancy("Python разработчик", 300000, 250000,
                       "https://hh.ru/vacancy/92467991",
                       "Разрабатывать и поддерживать микросервисы. Автоматизировать работу "
                       "с Wildberries или Яндекс Маркетом (API).",
                       "Удаленная работа")
    vacancies = [vacancy1, vacancy2]
    return vacancies


def test_json_processing(path, vacancy, vacancy_2):
    data = JsonProcessing(path)
    vacancy_json = data.read()
    assert len(vacancy_json) == 1
    data.write(vacancy_2)
    vacancy_json = data.read()
    assert len(vacancy_json) == 2
    assert vacancy_json[1]['responsibility'] == ("Разрабатывать и поддерживать микросервисы. Автоматизировать работу "
                                                 "с Wildberries или Яндекс Маркетом (API).")
    query = ['Яндекс']
    vacancy_json = data.get(query)
    assert vacancy_json[0]['responsibility'] == ("Разрабатывать и поддерживать микросервисы. Автоматизировать работу "
                                                 "с Wildberries или Яндекс Маркетом (API).")
    query = 'Яндекс'
    data.delete(query)
    vacancy_json = data.read()
    assert len(vacancy_json) == 1
