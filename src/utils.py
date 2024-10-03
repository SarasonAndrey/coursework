import json
import os
from json import JSONDecodeError
from typing import Any

financial_file = os.path.join('../data/operations.json')


def financial_transaction_data(financial_file: str) -> list[Any] | list:
    """Функция принимает на вход путь до JSON-файла и возвращаетсписок словарей с данными о финансовых транзакциях."""
    try:
        with open(financial_file, encoding="utf-8") as f:
            try:
                transactions = json.load(f)
            except JSONDecodeError:
                return []
        if not isinstance(transactions, list):
            return []
        return transactions

    except FileNotFoundError:
        return []


if __name__ == '__main__':
    print(financial_transaction_data(financial_file))
