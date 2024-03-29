from api.connector import HeadHunterAPI
from config import JSON_VACANCY
from database.json_processing import JsonProcessing
from utils import user_interaction

from vecancy_worcer.vecancy import Vacancy


def main() -> None:
    search_query, top_n, filter_words = user_interaction()
    path = JSON_VACANCY
    api_hh = HeadHunterAPI(search_query)
    data = api_hh.get_response()
    vacancies = Vacancy.initialization_hh(data)
    vacancies = list(sorted(vacancies, reverse=True))
    json_save = JsonProcessing(path)
    json_save.write(vacancies)
    request_response = json_save.get(filter_words)
    user_response_vacancy = Vacancy.initialization_json(request_response)
    for value in range(top_n):
        print(user_response_vacancy[value])


if __name__ == '__main__':
    main()
