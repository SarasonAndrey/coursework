from typing import Any

from src.widget import get_date, mask_account_card


def test_masks_account(account: Any) -> Any:
    assert mask_account_card(account) == 'Счет **4305'


def test_masks_number(number: Any) -> Any:
    assert mask_account_card(number) == 'Visa Platinum 7000 79** **** 6361'



def test_masks_() -> Any:
    assert get_date("2024-03-11T02:26:18.671407") == '11.03.2024'
