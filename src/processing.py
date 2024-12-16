from typing import Iterable

list_of_operations = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(inform_about_operations: Iterable, state_id: str = "EXECUTED") -> Iterable:
    """Функция фильтрующая операции по ключу state"""
    new_list_operations = []
    for operation in inform_about_operations:
        if operation.get("state") == state_id:
            new_list_operations.append(operation)
        else:
            continue
    return new_list_operations


print(filter_by_state(list_of_operations))


def sort_by_date(inform_about_operations: Iterable, reverse: bool = True) -> Iterable:
    """Функция сортирующая операции по дате"""
    operations_sorted_date = sorted(inform_about_operations, key=lambda x: x["date"], reverse=reverse)
    return operations_sorted_date


print(sort_by_date(list_of_operations))
