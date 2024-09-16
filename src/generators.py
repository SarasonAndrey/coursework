list_of_code = {
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
},


def filter_by_currency(transactions: list[dict], code: str = "USD"):
    list_of_code = []
    for values in code:
        if values.get("code") == code:
            list_of_code.append(values)
    return list_of_code


if __name__ == "__main__":
    print(filter_by_currency(list_of_code))
