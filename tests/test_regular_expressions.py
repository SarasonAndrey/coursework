from collections import Counter

import pytest

from src.regular_expressions import count_description, operations_search


@pytest.fixture
def trans_list():
    return [
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        },
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {
                "amount": "48223.05",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431",
        },
    ]


@pytest.fixture
def descript_dict():
    return [
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {
                "amount": "48223.05",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431",
        }
    ]


def test_operations_search(trans_list, descript_dict):
    """Тест проверяет работу функции по поиску транзакций с заданным описанием"""
    assert operations_search(trans_list, "Открытие вклада") == descript_dict


@pytest.fixture
def count_decript_dict():
    return Counter({"Перевод организации": 1, "Открытие вклада": 1})


def test_count_description(trans_list, count_decript_dict):
    """Тест проверяет работу функции по подсчету количества категорий по описанию"""
    assert count_description(trans_list, ["Перевод организации", "Открытие вклада"]) == count_decript_dict
