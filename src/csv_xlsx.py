import csv
from pathlib import Path
from typing import Any

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
path_csv = BASE_DIR / "data" / "transactions.csv"
path_exc = BASE_DIR / "data" / "transactions_excel.xlsx"


def read_csv(join_path_csv: Any) -> list[dict[str, str]] | list:
    """Функция принимает путь к файлу,  считывает информацию c CSV файла"""
    try:
        with open(path_csv, "r", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=";")
            header = next(reader)
            result = []
            for row in reader:
                row_dict = dict()
                for idx, item in enumerate(header):
                    row_dict[item] = row[idx]
                result.append(row_dict)
        return result
    except FileNotFoundError:
        transactions: list = []
        return transactions


def read_excel(path_exc: Any) -> list[dict[str, str]] | list:
    """Функция принимающая путь к файлу, считывает информацию c EXCEL файла"""
    try:
        reading_excel = pd.read_excel(path_exc)
        transaction_excel = []
        while True:
            for index, row in reading_excel.iterrows():
                list_file = {
                    "id": row["id"],
                    "state": row["state"],
                    "date": row["date"],
                    "amount": row["amount"],
                    "currency_name": row["currency_name"],
                    "currency_code": row["currency_code"],
                    "from": row["from"],
                    "to": row["to"],
                    "description": row["description"],
                }
                transaction_excel.append(list_file)
            return transaction_excel
    except Exception:
        return []


print(read_csv(path_csv))
print(read_excel(path_exc))
