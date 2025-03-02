from src.decorators import log


def test_log():
    """Тестироване работы декорированной функции"""

    @log(filename="")
    def my_function(x, y):
        return x + y

    result = my_function(1, 2)
    assert result == 3


def test_log_successful(capsys):
    """Тестирование вывода об успешном фыполнении функции в консоль"""

    @log(filename="")
    def my_function(x, y):
        return x + y

    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"


def test_log_exception(capsys):
    """Тестирование вывода об ошибке функции в консоль"""

    @log(filename="")
    def my_function(x, y):
        return x + y

    my_function(1, "2")
    captured = capsys.readouterr()
    assert captured.out == "my_function error: TypeError. Inputs: (1, '2'), {}\n"


def test_log_in_file(capsys):
    """Тестирование вывода об успешном выполнении функции в файл"""

    @log(filename="mylog.txt")
    def my_function(x, y):
        return x + y

    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"


def test_log_in_file_exception(capsys):
    """Тестирование вывода об ошибке фыполнении функции в файл"""

    @log(filename="mylog.txt")
    def my_function(x, y):
        return x + y

    my_function(1, "2")
    captured = capsys.readouterr()
    assert captured.out == "my_function error: TypeError. Inputs: (1, '2'), {}\n"
