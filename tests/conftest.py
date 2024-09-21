from typing import Any

import pytest


@pytest.fixture
def number() -> Any:
    return "700079228960000006361"


@pytest.fixture
def account() -> Any:
    return "73654108430135874305"


@pytest.fixture
def account1() -> Any:
    return "64686473678894779589"


@pytest.fixture
def account2() -> Any:
    return "35383033474447895560"


@pytest.fixture
def fo_filter_and_transaction1() -> Any:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        }
    ]


@pytest.fixture
def fo_filter_and_transaction2() -> Any:
    return [
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        }
    ]
