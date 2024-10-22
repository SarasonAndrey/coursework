import os

from src.csv_xlsx import read_csv, read_excel
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.regular_expressions import operations_search
from src.utils import financial_transaction_data
from src.widget import get_date, mask_account_card

path_to_file = os.path.join(os.path.dirname(__file__), "data", "operations.json")
join_path_csv = os.path.join(os.path.dirname(__file__), "data", "transactions.csv")
join_path_exc = os.path.join(os.path.dirname(__file__), "data", "transactions_excel.xlsx")


def main():
    print("Привет!\nДобро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    user_dialogue = input(
        "1. Получить информацию о транзакциях из JSON-файла"
        "\n2. Получить информацию о транзакциях из CSV-файла"
        "\n3. Получить информацию о транзакциях из XLSX-файла"
        "\nВвод: "
    )
    while True:
        if user_dialogue == "1":
            print("Для обработки выбран JSON-файл")
            transactions = financial_transaction_data(path_to_file)
            break
        elif user_dialogue == "2":
            print("Для обработки выбран CSV-файл")
            transactions = read_csv(join_path_csv)
            break
        elif user_dialogue == "3":
            print("Для обработки выбран XLSX-файл")
            transactions = read_excel(join_path_exc)
            break
        else:
            user_dialogue = input("Выбран несуществующий формат. Попробуйте еще раз\nВвод: ")

    state_operations = input(
        "Введите статус, по которому необходимо выполнить фильтрацию."
        "\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING.\nВвод: "
    ).upper()

    while True:
        if state_operations == "EXECUTED" or state_operations == "CANCELED" or state_operations == "PENDING":
            print(f"Операции отфильтрованы по статусу {state_operations}")
            state_operations_filter = filter_by_state(transactions, state_operations)
            break
        else:
            print(f"Статус операции {state_operations} недоступен.")
            state_operations = input(
                "Введите статус, по которому необходимо выполнить фильтрацию."
                "\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING.\nВвод: "
            ).upper()

    date_sort = input("Отсортировать операции по дате?\nВведите да или нет\nВвод: ").lower()

    while True:
        if date_sort == "да":
            reversing = input("Отсортировать по возрастанию или по убыванию?\nВвод: ").lower()
            if reversing == "по убыванию":
                sort_operations = sort_by_date(state_operations_filter, reverse=True)
                break
            elif reversing == "по возрастанию":
                sort_operations = sort_by_date(state_operations_filter)
                break
        else:
            print("Сортировка по дате не выбрана")
            sort_operations = state_operations_filter
            break

    sort_currency = input("Выводить только рублевые тразакции?\nВведите да или нет\nВвод: ").lower()

    while True:
        if sort_currency == "да":
            sort_currency_user = filter_by_currency(sort_operations, "руб.")
            break
        elif sort_currency == "нет":
            print("Фильтрация по валюте не выбрана")
            sort_currency_user = sort_operations
            break

    descriptions_filter = input(
        "Отфильтровать список транзакций по определенному слову в описании?\nВведите да или нет\nВвод: "
    ).lower()

    while True:
        if descriptions_filter == "да":
            search_string_user = input(
                "Выберите из списка доступные описания операций:\nПеревод организации\nОткрытие вклада"
                "\nПеревод со счета на счет\nПеревод с карты на счет\nПеревод с карты на карту\nВвод: "
            )
            final_filter_operations = operations_search(sort_currency_user, search_string_user)
            break
        elif descriptions_filter == "нет":
            print("Фильтрация по описанию операции не выбрана")
            final_filter_operations = sort_currency_user
            break

    print("Распечатываю итоговый список транзакций...")
    if len(final_filter_operations) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(final_filter_operations)}")
        for operation in final_filter_operations:
            if operation["description"] == "Открытие вклада":
                print(
                    f"{get_date(operation["date"])} Открытие вклада\n{mask_account_card(operation["to"])}"
                    f"\n Сумма: {operation["operationAmount"]["amount"]} "
                    f" {operation["operationAmount"]["currency"]["name"]}"
                )
            else:
                print(
                    f"{get_date(operation["date"])} {operation["description"]}"
                    f"\n{mask_account_card(operation["from"])} -> "
                    f"{mask_account_card(operation["to"])}\nСумма: {operation["operationAmount"]["amount"]}"
                    f" {operation["operationAmount"]["currency"]["name"]}"
                )


if __name__ == "__main__":
    main()
