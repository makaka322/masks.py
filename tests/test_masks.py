import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "number_card, expected_result_card",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("70007922896063614", "Неверные данные"),
        ("Hello", "Неверные данные"),
        ("12345", "Неверные данные"),
        ("", "Неверные данные"),
    ],
)
def test_get_mask_card_number(number_card, expected_result_card):
    assert get_mask_card_number(number_card) == expected_result_card


@pytest.mark.parametrize(
    "number_account, expected_result_account",
    [
        ("73654108430135874305", "**4305"),
        ("7365410843013587430573654108430135874305", "Неверные данные"),
        ("Hello", "Неверные данные"),
        ("12345", "Неверные данные"),
        ("", "Неверные данные"),
    ],
)
def test_get_mask_account(number_account, expected_result_account):
    assert get_mask_account(number_account) == expected_result_account
