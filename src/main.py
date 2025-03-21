from src.financial_transactions import reading_csv_file, reading_excel_file
from src.func_re import search_transactions
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.utils import get_financial_transactions
from src.widget import get_date, mask_account_card


def main():
    """Отвечает за основную логику проекта, связывает функциональности между собой."""
    print(
        """Привет! Добро пожаловать в программу работы 
    с банковскими транзакциями."""
    )

    while True:
        print(
            """Выберите необходимый пункт меню:
            1. Получить информацию о транзакциях из JSON-файла
            2. Получить информацию о транзакциях из CSV-файла
            3. Получить информацию о транзакциях из XLSX-файла"""
        )
        file_selection = input("Введите № пункта: ")
        if file_selection == "1":
            print("Для обработки выбран JSON-файл.")
            transactions_file = get_financial_transactions("..//data/operations.json")
            break
        elif file_selection == "2":
            print("Для обработки выбран CSV-файл.")
            transactions_file = reading_csv_file("..//data/transactions.csv")
            break
        elif file_selection == "3":
            print("Для обработки выбран XLSX-файл.")
            transactions_file = reading_excel_file("..//data/transactions_excel.xlsx")
            break
        else:
            print("Введен некорректный номер.")
            continue

    while True:
        print(
            """Введите статус, по которому необходимо выполнить фильтрацию. 
        Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""
        )

        status_selection = input().upper()
        if status_selection not in ["EXECUTED", "CANCELED", "PENDING"]:
            print(f"Статус операции {status_selection} недоступен.")
            continue
        print(f"Операции отфильтрованы по статусу {status_selection}")
        filtered_transactions = filter_by_state(transactions_file, status_selection)
        break

    print("Отсортировать операции по дате? Да/Нет")
    user_input_date = input("Введите да/нет: ").lower()

    if user_input_date == "да":
        print("Отсортировать по возрастанию или по убыванию? ")
        user_input_up_down = input("Введите по возрастанию/по убыванию: ").lower()
        if user_input_up_down == "по возрастанию":
            sort = sort_by_date(filtered_transactions, True)
        elif user_input_up_down == "по убыванию":
            sort = sort_by_date(filtered_transactions, False)
        else:
            print("Введен некорректный ответ.")
            return
    elif user_input_date == "нет":
        sort = filtered_transactions
    else:
        print("Введен некорректный ответ.")
        return

    print("Выводить только рублевые транзакции? Да/Нет")
    user_currency_filter = input("Введите да/нет: ").lower()

    if user_currency_filter == "да":
        sort = filter_by_currency(sort, "RUB")

    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    description_filter = input("Введите да/нет: ").lower()
    if description_filter == "да":
        print("Выберите категорию поиска? ")
        search = input("Открытие вклада/ Перевод организации/ Перевод с карты на карту: ").capitalize()
        sort = search_transactions(sort, search)

    print("Распечатываю итоговый список транзакций...")
    if sort:
        print(f"Всего банковских операций в выборке: {len(sort)}")
        for transaction in sort:
            date = get_date(transaction["date"])
            description = transaction["description"]
            card_to = mask_account_card(transaction["to"])
            try:
                operation_amount = transaction.get("operationAmount")
                if operation_amount is not None:
                    amount = round(float(operation_amount.get("amount")))
                    name = operation_amount.get("currency", {}).get("name")
                else:
                    amount = round(float(transaction.get("amount")))
                    name = transaction.get("currency_name")

            except (AttributeError, ValueError) as e:
                print(f"Ошибка при обработке транзакции: {e}")
                continue

            card_from = transaction.get("from")
            if card_from and str(card_from) != "nan":
                card_from = mask_account_card(str(card_from))
                print(f"{date} {description}\n{card_from} -> {card_to}\nСумма: {amount} {name}\n\n")
            else:
                print(f"{date} {description}\n{card_to}\nСумма: {amount} {name}\n\n")

    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")


if __name__ == "__main__":
    main()