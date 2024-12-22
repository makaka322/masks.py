import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "number, expected_result",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard7158300734726758", "Неверные данные"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("70007922896063614", "Неверные данные"),
        ("Hello", "Неверные данные"),
        ("12345", "Неверные данные"),
        ("", "Неверные данные"),
    ],
)
def test_mask_account_card(number, expected_result):
    assert mask_account_card(number) == expected_result


@pytest.mark.parametrize(
    "date, expected_date",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2024-03-11", "11.03.2024"),
        ("2019-05-22T16:26:18.598673", "22.05.2019"),

    ],
)
def test_get_date(date, expected_date):
    assert get_date(date) == expected_date
