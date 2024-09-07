def get_mask_card_number(card_number: str) -> str:
    """Функция принимает номер карты 12 цифр и возвращает ее маску
    :rtype: object
    """
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account: str) -> str:
    """Функция принимает номер счета 20 цифр и возвращает ее маску"""
    return f"**{account[-4:]}"


if __name__ == "__main__":
    print(get_mask_card_number("7000792289606361"))
    print(get_mask_account("73654108430135874305"))
