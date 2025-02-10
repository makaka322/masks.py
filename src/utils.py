import json
import logging
from json import JSONDecodeError

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(filename)s - %(levelname)s - %(message)s",
    filename="../logs/utils.log",
    filemode="w",
)

get_financial_transactions_logger = logging.getLogger()


def get_financial_transactions(path: str) -> list:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях."""
    get_financial_transactions_logger.info("Начало работы функции")
    try:
        with open(path, encoding="utf-8") as file:
            try:
                transactions = json.load(file)
                get_financial_transactions_logger.info("Создан список словарей финансовых транзакций")
                return transactions
            except JSONDecodeError:
                get_financial_transactions_logger.error("Ошибка файла с транзакциями")
                return []
    except FileNotFoundError:
        get_financial_transactions_logger.error("Файл с транзакциями не найден")
        return []
