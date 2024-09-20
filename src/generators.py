from typing import Any, Iterator

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
]


def filter_by_currency(data: list[dict], code: str = "USD") -> Iterator:
    """Функция выдает список трансакций с определенной валютой"""

    list_of_data = []
    for values in data:
        operation_amount = values.get("operationAmount")
        if operation_amount:
            currency = operation_amount.get("currency")
            if currency and currency.get("code") == code:
                list_of_data.append(values)
    usd_transactions = filter_by_currency(transactions, "USD")
    return usd_transactions


def transaction_descriptions(transactions_list: Any) -> Any:
    """Функция возвращает описания транзакций"""
    for transaction in transactions_list:
        yield transaction["description"]


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """Функция генерирует номер карты в форматате 'ХХХХ ХХХХ ХХХХ ХХХХ'"""
    for number in range(start, stop + 1):
        card_number = f"{number:016}"
        formatted_card_number = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
        yield formatted_card_number


# if __name__ == "__main__":
#     usd_transactions = filter_by_currency(transactions, "USD")
#     descriptions = transaction_descriptions(transactions)
#     gen_number = card_number_generator(1000, 1001)
#     for _ in range(5):
#         print(next(usd_transactions))
#         print(next(descriptions))
#         print(next(gen_number))
