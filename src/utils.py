import json
import os


def load_transactions(file_path):
    # Проверяем, существует ли файл и не пустой ли он
    if not os.path.isfile(file_path) or os.path.getsize(file_path) == 0:
        return []

    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            # Проверяем, является ли загруженные данные списком
            if isinstance(data, list):
                return data
            else:
                return []
    except json.JSONDecodeError:
        return []  # Возвращаем пустой список в случае ошибки парсинга JSON
    except Exception:
        return []  # Возвращаем пустой список в случае других ошибок
