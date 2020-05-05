"""Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала
для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего."""

from collections import namedtuple
from random import uniform
from statistics import mean


CompanyInfo = namedtuple('CompanyInfo', ['name', 'incomes'])


def test_data(n_companies):
    def quarters_income(_min: float, _max: float):
        for i in range(4):
            yield uniform(_min, _max)

    for i in range(n_companies):
        yield CompanyInfo(
            name=f'Company {i}',
            incomes=quarters_income(0, 100)
        )


def user_data():
    def quarters_income():
        for i in range(4):
            yield float(input(f'Quarter {i} income: >'))

    n_companies = int(input("Number of companies >"))
    for i in range(n_companies):
        yield CompanyInfo(
            name=input(f'Company {i+1} name: >'),
            incomes=quarters_income()
        )


if __name__ == '__main__':
    use_test_data = True  # swap to use user input or random data
    if use_test_data:
        data = test_data(10)
    else:
        data = user_data()

    companies = {
        company_info.name: sum(company_info.incomes)
        for company_info in data
    }
    mean_income = mean(companies.values())
    print(f'Mean annual income:\t{mean_income:.2f}')
    lower, upper = list(), list()
    for name, annual_income in companies.items():
        if annual_income < mean_income:
            lower.append(name)
        elif annual_income > mean_income:
            upper.append(name)
        else:  # it should not happen
            print(f'Company "{name}" has exactly mean annual income {annual_income:.2f}')

    print('Companies with annual income under mean')
    for name in lower:
        print(f'{name}:\t{companies[name]:.2f}')

    print('Companies with annual income above mean')
    for name in upper:
        print(f'{name}:\t{companies[name]:.2f}')
