from typing import Any

import pytest


@pytest.fixture
def number() -> Any:
    return 'Visa Platinum 7000792289606361'
    return 'Maestro 1596837868705199'
    return 'MasterCard 7158300734726758'
    return 'Visa Classic 6831982476737658'
    return 'Visa Platinum 8990922113665229'
    return 'Visa Gold 5999414228426353'


@pytest.fixture
def account() -> Any:
    return 'Счет 73654108430135874305'
    return 'Счет 64686473678894779589'
    return 'Счет 35383033474447895560'
