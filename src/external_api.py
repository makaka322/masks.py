import os
import requests
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')
API_URL = "https://api.apilayer.com/exchangerates_data"  # Убедитесь, что этот URL актуален

def convert_to_rub(amount, currency):
    if currency not in ['USD', 'EUR']:
        raise ValueError("Unsupported currency: Only USD or EUR are allowed")

    params = {
        'base': currency,
        'symbols': 'RUB',
        'apikey': API_TOKEN  # Ваш секретный токен
    }

    response = requests.get(f"{API_URL}/latest", params=params)
    response.raise_for_status()  # Поднимет ошибку, если запрос не успешен
    rates = response.json()['rates']
    return amount * rates['RUB']

def get_transaction_amount(transaction):
    amount = transaction['amount']
    currency = transaction['currency']

    if currency in ['USD', 'EUR']:
        return convert_to_rub(amount, currency)
    elif currency == 'RUB':
        return float(amount)
    else:
        raise ValueError("Unsupported currency: Only USD, EUR, and RUB are allowed")

# Пример транзакции
transaction = {
    'amount': 100,  # Сумма
    'currency': 'USD'  # Валюта
}

# Получаем сумму в рублях
try:
    rub_amount = get_transaction_amount(transaction)
    print(f"Сумма в рублях: {rub_amount}")
except ValueError as e:
    print(e)
except requests.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")  # Обработка ошибок сети
except Exception as err:
    print(f"An error occurred: {err}")  # Общее исключение
