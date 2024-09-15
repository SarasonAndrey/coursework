import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_mask() -> None:
    assert get_mask_card_number('7000792289606361') == '7000 79** **** 6361'


def test_mask_morenumbers() -> None:
    assert get_mask_card_number('700079228960000006361') == '7000 79** **** 6361'


def test_mask_nonnamber() -> None:
    with pytest.raises(AssertionError):
        assert get_mask_card_number('') == ''


def test_mask_() -> None:
    assert get_mask_account('73654108430135874305') == '**4305'


def test_mask_more_nambers() -> None:
    assert get_mask_account('736541084300000135874305') == '**4305'


def test_mask_fewer_nambers() -> None:
    assert get_mask_account('736541135874305') == '**4305'
