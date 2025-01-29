import os
import pytest
from unittest.mock import patch, Mock
from src.external_api import convert_to_rub, get_transaction_amount  # замените на имя вашего модуля


@pytest.fixture
def api_response_mock():
    """Создаем фикстуру для имитации ответа API."""
    return Mock(status_code=200, json=lambda: {'rates': {'RUB': 75.0}})


def test_convert_to_rub_success(api_response_mock):
    amount = 100
    currency = 'USD'

    # Патчим requests.get для возвращения mock-ответа
    with patch('requests.get', return_value=api_response_mock):
        result = convert_to_rub(amount, currency)

    assert result == 7500.0  # Ожидаем, что 100 * 75.0 = 7500


def test_convert_to_rub_invalid_currency():
    amount = 100
    currency = 'GBP'

    with pytest.raises(ValueError, match="Unsupported currency: Only USD or EUR are allowed"):
        convert_to_rub(amount, currency)


def test_get_transaction_amount_usd(api_response_mock):
    transaction = {
        'amount': 100,
        'currency': 'USD'
    }

    with patch('requests.get', return_value=api_response_mock):
        result = get_transaction_amount(transaction)

    assert result == 7500.0  # 100 * 75.0 = 7500


def test_get_transaction_amount_eur(api_response_mock):
    transaction = {
        'amount': 100,
        'currency': 'EUR'
    }

    # Предположим, что EUR к RUB также 75, например
    api_response_mock.json = lambda: {'rates': {'RUB': 80.0}}  # Изменяем курс в mock
    with patch('requests.get', return_value=api_response_mock):
        result = get_transaction_amount(transaction)

    assert result == 8000.0  # 100 * 80.0 = 8000


def test_get_transaction_amount_rub():
    transaction = {
        'amount': 100,
        'currency': 'RUB'
    }

    result = get_transaction_amount(transaction)

    assert result == 100.0  # Прямое возвращение суммы для RUB


def test_get_transaction_amount_invalid_currency():
    transaction = {
        'amount': 100,
        'currency': 'GBP'
    }

    with pytest.raises(ValueError, match="Unsupported currency: Only USD, EUR, and RUB are allowed"):
        get_transaction_amount(transaction)