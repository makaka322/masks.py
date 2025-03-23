import pandas as pd


def reading_csv_file(file_csv: str) -> list:
    """Функция считывает csv-файл и возвращает список словарей"""
    try:
        with open(file_csv, 'r', encoding='utf-8') as file:
            reader = pd.read_csv(file, delimiter=',')
        return reader.to_dict(orient='records')
    except FileNotFoundError:
        return []


def reading_excel_file(file_excel: str) -> list:
    """Функция считывает excel-файл и возвращает список словарей"""
    try:
        reader = pd.read_excel(file_excel)
        return reader.to_dict(orient='records')
    except FileNotFoundError:
        return []
