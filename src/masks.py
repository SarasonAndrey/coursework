def get_mask_card_number(card_number: str) -> str:
    """Функция принимает номер карты 12 цифр и возвращает ее маску
    :rtype: object
    """
    return (
        card_number[:4]
        + " "
        + card_number[4:6]
        + "*" * len(card_number[7:9])
        + " "
        + "*" * len(card_number[8:12])
        + " "
        + card_number[-4:]
    )


print(get_mask_card_number("7000792289606361"))


def get_mask_account(account: str) -> str:
    """Функция принимает номер счета 20 цифр и возвращает ее маску"""
    return "*" * len(account[-7:-5]) + account[-4:]


print(get_mask_account("73654108430135874305"))
