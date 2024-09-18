from typing import Any

transactions = {
    "id": 939719570,
    "state": "EXECUTED",
    "date": "2018-06-30T02:08:58.425572",
    "operationAmount": {
        "amount": "9824.07",
        "currency": {
            "name": "USD",
            "code": "USD"
        }
    },
    "description": "Перевод организации",
    "from": "Счет 75106830613657916952",
    "to": "Счет 11776614605963066702"
}, {
    "id": 939719570,
    "state": "EXECUTED",
    "date": "2018-06-30T02:08:58.425572",
    "operationAmount": {
        "amount": "9824.07",
        "currency": {
            "name": "USS",
            "code": "USS"
        }
    },
    "description": "Перевод организации",
    "from": "Счет 75106830613657916952",
    "to": "Счет 11776614605963066702"
}


def filter_by_currency(data: list[dict[str, Any]], code: str = "USS") -> list[dict[str, Any]]:
    """Функция выдает список трансакций с определенной валютой"""

    list_of_data = []
    for values in data:
        if values.get("operationAmount").get("currency").get("code") == code:
            list_of_data.append(values)
    return list_of_data


if __name__ == "__main__":
    print(filter_by_currency(transactions))
