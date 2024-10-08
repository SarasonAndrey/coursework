from typing import Any

import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "number, expected_result",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Счет 35383033474447895560", "Счет **5560"),
    ],
)
def test_widget(number: Any, expected_result: Any) -> Any:
    assert mask_account_card(number) == expected_result


def test_widget_error_name() -> Any:
    with pytest.raises(AssertionError):
        assert mask_account_card("MsterCard 7158300734726758") == "MasterCard 7158 30** **** 6758"


def test_widget_data() -> Any:
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


def test_widget_non_data() -> Any:
    with pytest.raises(AssertionError):
        assert get_date("") == ""


def test_widget_incomplete_data() -> Any:
    assert get_date("2024-03-31") == "31.03.2024"


def test_widget_unformatted_data() -> Any:
    with pytest.raises(AssertionError):
        assert get_date("31/03/2024") == "31.03.2024"
