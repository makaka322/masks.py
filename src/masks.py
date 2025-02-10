import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s - %(levelname)s - %(message)s',
                    filename='../logs/masks_log.log',
                    filemode='w')

mask_card_number_logger = logging.getLogger()
mask_account_logger = logging.getLogger()

def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера карты"""
    mask_card_number_logger.info('Запуск маскировки номера карты')
    if card_number.isdigit() and len(card_number) == 16:
        mask_card_number_logger.info('Маска номера карты создана')
        return f"{card_number[0: 4]} {card_number[4: 6]}{"*" * 2} {"*" * 4} {card_number[-4:]}"
    else:
        mask_card_number_logger.info('Неверные данные')
        return "Неверные данные"


def get_mask_account(account_number: str) -> str:
    """Функция маскировки номера счета"""
    mask_account_logger.info('Запуск маскировки номера счета')
    if account_number.isdigit() and len(account_number) == 20:
        mask_account_logger.info('Маска номера счета создана')
        return f"{"*" * 2}{account_number[-4::]}"
    else:
        mask_account_logger.info('Неверные данные')
        return "Неверные данные"

# Пример вызова функций
if __name__ == "__main__":
    print(get_mask_card_number("1625344646464646"))
    print(get_mask_account("81726645454545454545"))
