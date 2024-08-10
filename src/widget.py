def mask_account_car(card_type: str, card_number: str, account: str, account_numbers: str) -> str:
    """Функция  которая умеет обрабатывать информацию о картах и о счетах"""
    if mask_account_car == card_type:
        return f"{card_type[:]} {card_number[:4]} {card_number[4:6]}** ****{card_number[-4:]}"

    else:
        return f"{account[:]} **{account_numbers[-4:]}"


def get_date(data: str) -> str:
    return f"{data[8:10]}.{data[5:7]}.{data[:4]}"
