from __future__ import annotations

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(name: str) -> str | None:
    """Функция  которая скрывает информацию о картах и счетах"""
    if "Счет" in name:
        card = get_mask_account(name[-20:])
        new_card = name.replace(name[-20:], card)

        return new_card

    else:
        card = get_mask_card_number(name[-16:])
        new_card = name.replace(name[-16:], card)

        return new_card


def get_date(data: str) -> str | None:
    """Функция принимает на вход строку с датой в формате 2024-03-11T02:26:18.671407
    и возвращает строку с датой в формате ДД.ММ.ГГГГ"""
    return f"{data[8:10]}.{data[5:7]}.{data[:4]}"

# if __name__ == "__main__":
#     print(get_date("2024-03-11T02:26:18.671407"))
#     print(mask_account_card("Счет 64686473678894779589"))
#     print(mask_account_card("MasterCard 7158300734726758"))
#     print(mask_account_card("Visa Gold 5999414228426353"))
