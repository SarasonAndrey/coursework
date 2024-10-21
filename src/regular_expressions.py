import re
from collections import Counter


def data_search(transactions: list[dict], search_string: str) -> list[dict]:
    """Функцию, принимает список словарей с данными о банковских операциях
    и строку поиска, а возвращать список словарей."""
    pattern = re.compile(search_string, re.IGNORECASE)
    operations_filter = []
    for transaction in transactions:
        if re.search(pattern, transaction["description"]):
            operations_filter.append(transaction)
    return operations_filter


def categories_and_values(transactions: list[dict], categories: list) -> dict:
    """Функция принимает на вход список словарей, список категорий и возвращает словарь,
    где ключи — это названия категорий, а значения — это количество операций в каждой категории."""
    categories_dict = []
    for transaction in transactions:
        descript = transaction["description"]
        for category in categories:
            if re.search(category, descript, re.IGNORECASE):
                categories_dict.append(category)
    categories_and_values = Counter(categories_dict)
    return categories_and_values
