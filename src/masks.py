import logging

# Создаем основные конфигурации logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(name)s %(levelname)s %(message)s",
    filename="../logs/masks.log",
    filemode="w",
    encoding="utf-8",
)
# Создаем логи для отдельных функций
card_number_logger = logging.getLogger("app.card_number")
mask_account_logger = logging.getLogger("app.mask_account")




def get_mask_card_number(card_number: str) -> str:
    """Функция принимает номер карты 12 цифр и возвращает ее маску
    :rtype: object
    """
    card_number_logger.info("Ввод номера карты и его маскировка")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account: str) -> str:
    """Функция принимает номер счета 20 цифр и возвращает ее маску"""
    mask_account_logger.info("Ввод номера счета и его маскировка")
    return f"**{account[-4:]}"


if __name__ == "__main__":
    print(get_mask_card_number("7000792289606361"))
    print(get_mask_account("73654108430135874305"))
