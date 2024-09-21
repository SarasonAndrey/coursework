from typing import Any

import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_mask(number: Any) -> Any:
    assert get_mask_card_number(number) == "7000 79** **** 6361"


def test_mask_morenumbers() -> None:
    assert get_mask_card_number("700079228960000006361") == "7000 79** **** 6361"


def test_mask_nonnamber() -> None:
    with pytest.raises(AssertionError):
        assert get_mask_card_number("") == ""


def test_mask_1(account: Any) -> Any:
    assert get_mask_account(account) == "**4305"


def test_mask_2(account1: Any) -> Any:
    assert get_mask_account(account1) == "**9589"


def test_mask_3(account2: Any) -> Any:
    assert get_mask_account(account2) == "**5560"


def test_mask_more_nambers() -> None:
    assert get_mask_account("736541084300000135874305") == "**4305"


def test_mask_fewer_nambers() -> None:
    assert get_mask_account("736541135874305") == "**4305"
