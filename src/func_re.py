import re
from collections import Counter

from src.financial_transactions import reading_csv_file, reading_excel_file
from src.utils import get_financial_transactions

json_file = get_financial_transactions('../data/operations.json')
csv_file = reading_csv_file('../data/transactions.csv')
excel_file = reading_excel_file('../data/transactions_excel.xlsx')


def search_transactions(transactions: list[dict], search_string: str) -> list[dict]:
    """Функция, принимает список словарей с данными о банковских операциях и строку поиска, а возвращает
    список словарей, у которых в описании есть данная строка"""
    result = []
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)
    for transaction in transactions:
        if isinstance(transaction, dict):
            desc = transaction.get("description", "")
            if isinstance(desc, str):
                if re.search(pattern, desc):
                    result.append(transaction)

    return result


def get_count_transactions(transactions: list[dict], categories: list) -> dict:
    """Функция принимает список словарей с данными о банковских операциях и список категорий операций, а возвращает
    словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой категории."""
    description = []
    for transaction in transactions:
        if transaction["description"] in categories:
            description.append(transaction["description"])
    counted = dict(Counter(description))
    return counted
