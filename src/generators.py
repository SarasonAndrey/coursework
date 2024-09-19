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


def filter_by_currency(data: list[dict[str, Any]], code: str | None = "USD") -> Iterator:
    """Функция выдает список трансакций с определенной валютой"""

    list_of_data = []
    for values in data:
        if values.get("operationAmount").get("currency").get("code") == code:
            list_of_data.append(values)
    yield list_of_data


def transaction_descriptions(transactions: Any) -> Any:
    """Функция возвращает описания транзакций"""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(number: int, end: int) -> str:
    """Функция генерирует номер карты"""
    for number in range(1, end + 1):
        card_number = str(number)
        while len(card_number) < 16:
            card_number = "0" + card_number

        formatted_card_number = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"

        yield (formatted_card_number)


if __name__ == "__main__":
    usd_transactions = filter_by_currency(transactions, "USD")
    descriptions = transaction_descriptions(transactions)
    gen_number = card_number_generator(1, 5)
    for _ in range(5):
        print(next(usd_transactions))
        print(next(descriptions))
        print(next(gen_number))
