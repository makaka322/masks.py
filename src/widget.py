from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_details: str) -> str:
    """Функция маскирует номер счета/карты"""
    number = card_details.split(" ")[-1]
    if number.isdigit() and len(number) == 16:
        masks = get_mask_card_number(number)
        return f"{card_details[:-16]}{masks}"
    elif number.isdigit() and len(number) == 20:
        masks = get_mask_account(number)
        return f"{card_details[:-20]}{masks}"
    else:
        return "Неверные данные"


def get_date(user_date: str) -> str:
    """Функция для преобразования даты"""
    return f"{user_date[8:10]}.{user_date[5:7]}.{user_date[0:4]}"


print(mask_account_card("Maestro 1596837868705199"))
print(mask_account_card("Счет 35383033474447895560"))
print(get_date("2024-03-11T02:26:18.671407"))
