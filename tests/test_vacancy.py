import pytest

from config import TEST_JSON
from vecancy_worcer.vecancy import Vacancy


@pytest.fixture
def response_hh():
    return {
        'alternate_url': 'https://hh.ru/search/vacancy?area=113&enable_snippets=true&items_on_page=2&only_with_salary=true&search_field=name&text=python',
        'arguments': None,
        'clusters': None,
        'fixes': None,
        'found': 404,
        'items': [{'accept_incomplete_resumes': False,
                   'accept_temporary': False,
                   'address': None,
                   'adv_context': None,
                   'adv_response_url': None,
                   'alternate_url': 'https://hh.ru/vacancy/92363159',
                   'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=92363159',
                   'archived': False,
                   'area': {'id': '70',
                            'name': 'Оренбург',
                            'url': 'https://api.hh.ru/areas/70'},
                   'contacts': None,
                   'created_at': '2024-01-29T17:28:15+0300',
                   'department': None,
                   'employer': {'accredited_it_employer': False,
                                'alternate_url': 'https://hh.ru/employer/10741524',
                                'id': '10741524',
                                'logo_urls': None,
                                'name': 'Ryzen',
                                'trusted': False,
                                'url': 'https://api.hh.ru/employers/10741524',
                                'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=10741524'},
                   'employment': {'id': 'probation', 'name': 'Стажировка'},
                   'experience': {'id': 'noExperience', 'name': 'Нет опыта'},
                   'has_test': False,
                   'id': '92363159',
                   'insider_interview': None,
                   'is_adv_vacancy': False,
                   'name': 'Стажер-разработчик Python',
                   'premium': False,
                   'professional_roles': [{'id': '96',
                                           'name': 'Программист, разработчик'}],
                   'published_at': '2024-01-29T17:28:15+0300',
                   'relations': [],
                   'response_letter_required': False,
                   'response_url': None,
                   'salary': {'currency': 'RUR',
                              'from': None,
                              'gross': False,
                              'to': None},
                   'schedule': {'id': 'fullDay', 'name': 'Полный день'},
                   'snippet': {'requirement': 'Отличные коммуникативные навыки. '
                                              'Любовь к коду. Быть активным и '
                                              'внедрять эффективные решения.',
                               'responsibility': 'Внедрять новые инженерные решения. '
                                                 'Поддерживать текущий проект. '
                                                 'Разработка десктоп ПО по нашим '
                                                 'лекалам <highlighttext>python</highlighttext>.'},
                   'sort_point_distance': None,
                   'type': {'id': 'open', 'name': 'Открытая'},
                   'url': 'https://api.hh.ru/vacancies/92363159?host=hh.ru',
                   'working_days': [],
                   'working_time_intervals': [],
                   'working_time_modes': []},
                  {'accept_incomplete_resumes': False,
                   'accept_temporary': True,
                   'address': None,
                   'adv_context': None,
                   'adv_response_url': None,
                   'alternate_url': 'https://hh.ru/vacancy/91664414',
                   'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=91664414',
                   'archived': False,
                   'area': {'id': '1',
                            'name': 'Москва',
                            'url': 'https://api.hh.ru/areas/1'},
                   'contacts': None,
                   'created_at': '2024-01-30T15:59:12+0300',
                   'department': None,
                   'employer': {'accredited_it_employer': False,
                                'alternate_url': 'https://hh.ru/employer/9887405',
                                'id': '9887405',
                                'logo_urls': {'240': 'https://hhcdn.ru/employer-logo/6035590.jpeg',
                                              '90': 'https://hhcdn.ru/employer-logo/6035589.jpeg',
                                              'original': 'https://hhcdn.ru/employer-logo-original/1103745.jpg'},
                                'name': 'WBPROD',
                                'trusted': True,
                                'url': 'https://api.hh.ru/employers/9887405',
                                'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=9887405'},
                   'employment': {'id': 'full', 'name': 'Полная занятость'},
                   'experience': {'id': 'between1And3', 'name': 'От 1 года до 3 лет'},
                   'has_test': False,
                   'id': '91664414',
                   'insider_interview': None,
                   'is_adv_vacancy': False,
                   'name': 'Backend разработчик Python',
                   'premium': False,
                   'professional_roles': [{'id': '96',
                                           'name': 'Программист, разработчик'}],
                   'published_at': '2024-01-30T15:59:12+0300',
                   'relations': [],
                   'response_letter_required': False,
                   'response_url': None,
                   'salary': {'currency': 'RUR',
                              'from': 80000,
                              'gross': False,
                              'to': 180000},
                   'schedule': {'id': 'fullDay', 'name': 'Полный день'},
                   'show_logo_in_search': None,
                   'snippet': {'requirement': 'Глубокие знания и опыт работы с '
                                              'технологиями из нашего стека. '
                                              '(<highlighttext>Python</highlighttext> '
                                              '3.11, FastApi, Celery, Asyncio, '
                                              'Aiohttp, Pytest. Docker, RabbitMQ). ',
                               'responsibility': 'Разработка пользовательских '
                                                 'интерфейсов. Участие в '
                                                 'проектировании, выборе и доработке '
                                                 'архитектурных и технологических '
                                                 'решений. Настройка страниц и '
                                                 'компонентов. Кастомизация внешнего '
                                                 'вида...'},
                   'sort_point_distance': None,
                   'type': {'id': 'open', 'name': 'Открытая'},
                   'url': 'https://api.hh.ru/vacancies/91664414?host=hh.ru',
                   'working_days': [],
                   'working_time_intervals': [],
                   'working_time_modes': []}],
        'page': 0,
        'pages': 202,
        'per_page': 2,
        'suggests': None}

@pytest.fixture
def vacancies_json():
    return [
  {
    "name": "Senior Python разработчик",
    "salary_to": 370000,
    "salary_from": 300000,
    "alternate_url": "https://hh.ru/vacancy/92135217",
    "responsibility": "Portal Bilet - e-commerce платформа, которая занимается продажей билетов и покрывает все сферы event-сегмента, от небольшого локального события до...",
    "schedule": "Удаленная работа"
  },
  {
    "name": "Системный программист / разработчик Python",
    "salary_to": 350000,
    "salary_from": 200000,
    "alternate_url": "https://hh.ru/vacancy/92323149",
    "responsibility": "Управлять задачами, командами, проектами, разработкой и внедрением усовершенствований. Отслеживать изменения, компоненты и версии. Настраивать собственные бизнес-процессы и автоматизировать деятельность. ",
    "schedule": "Удаленная работа"
  }
]

def test_initialization_hh(response_hh):
    vacancies = Vacancy.initialization_hh(response_hh)
    assert len(vacancies) == 2
    assert vacancies[0].name == 'Стажер-разработчик Python'
    assert vacancies[0].salary_from == 0
    assert vacancies[0].salary_to == 0

    assert vacancies[1].name == 'Backend разработчик Python'
    assert vacancies[1].salary_from == 80000
    assert vacancies[1].salary_to == 180000

    vacancies = list(sorted(vacancies, reverse=True))
    assert vacancies[0].name == 'Backend разработчик Python'
    assert vacancies[0].salary_from == 80000
    assert vacancies[0].salary_to == 180000

    assert vacancies[1].name == 'Стажер-разработчик Python'
    assert vacancies[1].salary_from == 0
    assert vacancies[1].salary_to == 0


def test_initialization_json(vacancies_json):
    vacancies = Vacancy.initialization_json(vacancies_json)
    assert len(vacancies) == 2
