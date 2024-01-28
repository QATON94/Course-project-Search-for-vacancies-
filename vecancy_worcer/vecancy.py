class Vacancy:
    """
    Вакансия
    """

    def __init__(self, name: str, salary_to: float, salary_from: float, alternate_url: str, responsibility: str,
                 schedule: str):
        """
        :param name: Название
        :param salary_to: Зарплата до
        :param salary_from: Зарплата от
        :param alternate_url: URL адрес
        :param responsibility: Описание
        :param schedule: Рабочие часы
        """
        self.name = name
        self.salary_to = salary_to
        self.salary_from = salary_from
        self.alternate_url = alternate_url
        self.responsibility = responsibility
        self.schedule = schedule

    @classmethod
    def initialization_json(cls, data: list):
        """
        Инициализация атрибутов
        :param data:
        :return:
        """
        vacancy_list = []
        for item in data:
            salary_from, salary_to = validate_salary(item['salary'])
            snippet: str = validate_responsibility(item['snippet']['responsibility'])
            vacancy = cls(
                name=item['name'],
                salary_to=salary_to,
                salary_from=salary_from,
                alternate_url=item['alternate_url'],
                responsibility=snippet,
                schedule=item['schedule']['name']
            )
            vacancy_list.append(vacancy)
        return vacancy_list

    @property
    def avg_salary(self):
        return (self.salary_from + self.salary_to) / 2

    def __gt__(self, other):
        return self.avg_salary > other.avg_salary

    def __lt__(self, other):
        return self.avg_salary < other.avg_salary


def validate_salary(salary: dict | None):
    if isinstance(salary, dict):
        from_ = salary.get('from', 0)
        if from_ is None:
            from_ = 0
        to_ = salary.get('to', 0)
        if to_ is None:
            to_ = 0
        return from_, to_
    return 0, 0

def validate_responsibility(responsibility: str | None):
    if isinstance(responsibility, str):
        responsibility = responsibility.replace('<highlighttext>Python</highlighttext>', 'Python')
        responsibility = responsibility.replace('<highlighttext>python</highlighttext>', 'python')
        return responsibility
    return ''
