from src.moduls import HeadHunterAPI, Vacancy, JSONSaver
from src.utils import user_interaction


def main():
    # search_query, top_n, filter_words = user_interaction()
    api_hh = HeadHunterAPI('python', 50, 'что то')
    data = api_hh.get_vacancies()
    vacancy = Vacancy.initialization(data)
    json_saver = JSONSaver()
    json_saver.add_vacancy(vacancy)


if __name__ == '__main__':
    main()
