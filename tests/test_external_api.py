from unittest.mock import patch

import pytest

from src.external_api import transaction_amount


@pytest.fixture
def transaction_fix_rub():
    return {
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


@pytest.fixture
def transaction_fix():
    return {
        "id": 633268359,
        "state": "EXECUTED",
        "date": "2019-07-12T08:11:47.735774",
        "operationAmount": {
            "amount": "2631.44",
            "currency": {"name": "EUR", "code": "EUR"},
        },
        "description": "Перевод организации",
        "from": "Visa Gold 3589276410671603",
        "to": "Счет 96292138399386853355",
    }


def test_transaction_amount_rub(transaction_fix_rub):
    assert transaction_amount(transaction_fix_rub) == 48223.05


@patch("requests.get")
def test_transaction_amount_mock(mock_get, transaction_fix):
    mock_get.return_value.json.return_value = {
        "success": True,
        "query": {"from": "EUR", "to": "RUB", "amount": 2631.44},
        "info": {"timestamp": 1726949044, "rate": 103.07316},
        "date": "2024-09-21",
        "result": 271230.83615,
    }
    assert transaction_amount(transaction_fix) == 271230.83615
