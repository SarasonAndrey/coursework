import json
import logging
import os
from json import JSONDecodeError
from typing import Any

# Создаем основные конфигурации logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(name)s %(levelname)s %(message)s",
    filename="../logs/utils.log",
    filemode="w",
    encoding="utf-8",
)
# Создаем логи для отдельных частей функции
open_file_logger = logging.getLogger("app.file")
find_file_logger = logging.getLogger("find.file")
convert_file_logger = logging.getLogger("convert.file")
financial_file = os.path.join("../data/operations.json")


def financial_transaction_data(financial_file: str) -> list[Any] | list:
    """Функция принимает на вход путь до JSON-файла и возвращаетсписок словарей с данными о финансовых транзакциях."""
    try:
        with open(financial_file, encoding="utf-8") as f:
            open_file_logger.info("Открытие файла json")
            try:
                transactions = json.load(f)
                convert_file_logger.info("Конвертирование в Python файл")
            except JSONDecodeError:
                convert_file_logger.error("Ошибка конвертации")
                return []
        if not isinstance(transactions, list):
            open_file_logger.error("Ошибка чтения файла")
            return []
        return transactions

    except FileNotFoundError:
        find_file_logger.error("Файл не найден")
        return []


if __name__ == "__main__":
    print(financial_transaction_data(financial_file))
