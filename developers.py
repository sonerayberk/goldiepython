""" Playing with CSV.

    Data set:   40,000 answer records from DOU (developers of Ukraine) from May 2015 until June 2018.
    Source:     https://github.com/devua/csv/tree/master/salaries.
"""

import csv
import glob
from collections import defaultdict
from functools import reduce, partial
from operator import add
from typing import NamedTuple

Language = NamedTuple('Language', [('language', str), ('experience', str), ('age', int), ('salary', float)])

favo_lang = 'Python'

_languages = []
accumulated_records = defaultdict(list)

for filename in glob.glob('data/*_*.csv'):
    with open(filename) as f:
        reader = csv.reader(f)
        header = next(reader)
        for (
            position, language, specialization, total_experience, current_experience, salary,
            salary_changes, city, company_size, company_type, gender, age, education,
            *args,  # other arguments: university, is_student, english_level, field, date_of_creation, user_agent
        ) in reader:
            _language = Language(language, total_experience, int(age), float(salary))
            accumulated_records[language].append(_language)
            _languages.append(language)

languages = set(_languages)
records = {language: tuple(args) for language, args in accumulated_records.items()}


def record_language(language: str) -> dict:
    assert language in languages
    return records[language]


def avg_(language: str, key: str) -> float:
    """ helper avg function. """
    assert key in Language._fields
    data = record_language(language)
    values = [getattr(record, key) for record in data]
    return reduce(partial(add), values) / len(values)


def avg_salary(language: str) -> float:
    return avg_(language, key='salary')


def avg_age(language: str) -> float:
    return avg_(language, key='age')

avg_salaries = {lang: avg_salary(lang) for lang in languages}

if __name__ == '__main__':
    for lang, items in records.items():
        for item in items:
            pass  # print(item)
        print(f'\nLANGUAGE: {lang}')
        print(f'Average salary: {avg_salary(lang)}')
        print(f'Average age: {avg_age(lang)}\n')
