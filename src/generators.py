from typing import Any


def filter_by_currency(transactions_list: Any, currency: str) -> Any:
    """Функция, возвращающая итератор, где валюта операции соответствует заданной"""
    if len(transactions_list) > 0:
        filtered_transactions = filter(
            lambda transaction: (
                    transaction.get("operationAmount") is not None and
                    transaction["operationAmount"].get("currency") is not None and
                    transaction["operationAmount"]["currency"].get("code") == currency
            ),
            transactions_list,
        )
        return filtered_transactions
    else:
        return "Список пустой!"


def transaction_descriptions(transactions_list: Any) -> Any:
    """Функция выводит описание операции"""
    if len(transactions_list) > 0:
        for operation in transactions_list:
            yield operation.get("description")
    else:
        yield "Список пустой!"


def card_number_generator(start: int, stop: int) -> Any:
    """Функция, которая выдает номера банковских карт"""
    while start <= stop:
        card_number = str(start)
        while len(card_number) < 16:
            card_number = "0" + card_number
        formatted_card_number = (
            card_number[:4] + " " + card_number[4:8] + " " + card_number[8:12] + " " + card_number[12:]
        )
        yield formatted_card_number
        start += 1
