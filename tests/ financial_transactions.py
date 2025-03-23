from unittest.mock import patch

import pandas as pd

import pytest

from src.financial_transactions import reading_csv_file, reading_excel_file


@pytest.fixture
def test_df() -> pd.DataFrame:
    """Фикстура, создающая тестовый DataFrame"""

    test_dict = {
        "id": [650703.0, 3598919.0],
        "state": ["EXECUTED", "EXECUTED"],
        "date": ["2023-09-05T11:30:32Z", "2020-12-06T23:00:58Z"],
        "amount": [16210.0, 29740.0],
        "currency_name": ["Sol", "Peso"],
        "currency_code": ["PEN", "COP"],
        "from": ["Счет 58803664561298323391", "Discover 3172601889670065"],
        "to": ["Счет 39745660563456619397", "Discover 0720428384694643"],
        "description": ["Перевод организации", "Перевод с карты на карту"]
    }
    return pd.DataFrame(test_dict)


@patch('src.financial_transactions.pd.read_csv')
def test_reading_csv_file(mock_read, test_df):
    mock_read.return_value = test_df
    result = reading_csv_file('../data/transactions.csv')
    expected = test_df.to_dict(orient='records')
    assert result == expected


def test_reading_transaction_with_incorrect_path_csv():
    assert reading_csv_file("") == []


@patch('src.financial_transactions.pd.read_excel')
def test_reading_excel_file(mock_read, test_df):
    mock_read.return_value = test_df
    result = reading_excel_file('../data/transactions_excel.xlsx')
    expected = test_df.to_dict(orient='records')
    assert result == expected


def test_reading_transaction_with_incorrect_path_excel():
    assert reading_excel_file("") == []