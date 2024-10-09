import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def transaction_amount(transaction: dict) -> float:
    """Функция конвертации"""
    amount = transaction["operationAmount"]["amount"]
    code = transaction["operationAmount"]["currency"]["code"]
    if transaction["operationAmount"]["currency"]["code"] != "RUB":
        response = requests.get(
            f"https://api.apilayer.com/exchangerates_data/convert?to={"RUB"}&from={code}&amount={amount}",
            headers={"apikey": f"{API_KEY}"},
        )
        result = response.json()
        return float(result["result"])
    else:
        return float(amount)
