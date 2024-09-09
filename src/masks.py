def get_mask_card_number(card_number: str) -> str:
    """Функция принимает номер карты и выдает замаскированную версию"""
    if card_number.isdigit() and len(card_number) == 16:
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
    else:
        return "Неверные данные"


def get_mask_account(account_number: str) -> str:
    """Функция принимает номер счета и выдает замаскированную версию"""
    if account_number.isdigit() and len(account_number) == 20:
        return f"**{account_number[-4:]}"
    else:
        return "Неверные данные"


print(get_mask_card_number("1625344646464646"))
print(get_mask_account("81726645454545454545"))
