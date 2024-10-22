import re
from collections import Counter


def operations_search(transactions: list[dict], search_string: str) -> list[dict]:
    """Функция принимает на вход список транзакций и строку поиска и возвращает список транзакций,
    в описании которых содержится искомая строка"""
    pattern = re.compile(search_string, re.IGNORECASE)
    operations_filter = []
    for transaction in transactions:
        if re.search(pattern, transaction["description"]):
            operations_filter.append(transaction)
    return operations_filter


def count_description(transactions: list[dict], categories: list) -> dict:
    """Функция принимает на вход список транзакций и список категорий и возвращает словарь,
    где ключи это описание операций, а значения это количество операций в каждой категории
    """
    categories_dict = []
    for transaction in transactions:
        descript = transaction["description"]
        for category in categories:
            if re.search(category, descript, re.IGNORECASE):
                categories_dict.append(category)
    counted_description = Counter(categories_dict)
    return counted_description
