from src.masks import get_mask_card_number, get_mask_account


def test_mask() -> None:
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"


def test_mask_() -> None:
    assert get_mask_account("73654108430135874305") == "**4305"
