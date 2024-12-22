import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(inform_about_transactions):
    generator = filter_by_currency(inform_about_transactions, "USD")
    assert next(generator) == {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        }
    assert next(generator) == {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        }
    assert next(generator) == {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        }


def test_filter_by_currency_eur(inform_about_transactions):
    assert list(filter_by_currency(inform_about_transactions, "EUR")) == []


def test_filter_by_currency_(inform_about_transactions):
    assert filter_by_currency([], "USD") == "Список пустой!"


def test_transaction_descriptions(inform_about_transactions):
    generator = transaction_descriptions(inform_about_transactions)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"


def test_transaction_descriptions_():
    generator = list(transaction_descriptions([]))
    assert generator == ["Список пустой!"]


@pytest.mark.parametrize(
    "start, stop, result",
    [
        (0, 0, "0000 0000 0000 0000"),
        (5, 5, "0000 0000 0000 0005"),
        (10, 10, "0000 0000 0000 0010"),
    ],
)
def test_card_number_generator(start, stop, result):
    generator = list(card_number_generator(start, stop))
    assert generator == [result]
