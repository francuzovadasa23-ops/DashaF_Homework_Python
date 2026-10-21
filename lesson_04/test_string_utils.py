import pytest
from string_utils import StringUtils


@pytest.mark.positive
@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("привет", "Привет"),             # строка в нижнем регистре
        ("Привет", "Привет"),             # строка уже с заглавной буквой
        # строка из нескольких слов с разными регистрами
        ("hello World", "Hello world")
    ])
def test_capitalize_positive(input_text, expected_output):
    string = StringUtils()
    assert string.capitalize(input_text) == expected_output


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("123abc", "123abc"),    # строка начинается с цифр
        ("", ""),                # пустая строка
        ("  ", "  ")             # строка из пробелов
    ])
def test_capitalize_negative(input_text, expected_output):
    string = StringUtils()
    assert string.capitalize(input_text) == expected_output


@pytest.mark.positive
@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        (" привет", "привет"),              # пробел только в начале строки
        ("привет", "привет"),               # строка без пробелов
        # строка из нескольких слов, много пробелов в начале
        ("  hello world", "hello world")
    ])
def test_trim_positive(input_text, expected_output):
    string = StringUtils()
    assert string.trim(input_text) == expected_output


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("", ""),                               # пустая строка
        (" ", ""),                              # строка только из пробелов
        ("привет  ", "привет  "),               # пробелы в конце
        ("  hello world  ", "hello world  ")    # разные регистры
    ])
def test_trim_negative(input_text, expected_output):
    string = StringUtils()
    assert string.trim(input_text) == expected_output


@pytest.mark.positive
@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [
        ("Привет", "П", True),    # символ в начале строки
        ("Привет", "т", True),    # символ в конце строки
        ("Привет", "и", True),    # символ в середине строки
    ])
def test_contains_positive(input_text, symbol, expected_output):
    string = StringUtils()
    assert string.contains(input_text, symbol) == expected_output


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [
        ("Привет", "А", False),    # символа нет
        ("Привет", "п", False),    # не совпадает регистр
        ("", "и", False),          # пустая строка
    ])
def test_contains_negative(input_text, symbol, expected_output):
    string = StringUtils()
    assert string.contains(input_text, symbol) == expected_output


@pytest.mark.positive
@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [
        ("Привет", "П", "ривет"),    # удалить первый символ
        ("Привет", "т", "Приве"),    # удалить последний символ
        ("Hello", "l", "Heo"),
        # удалить символ, который встречается несколько раз
        ("Python", "hon", "Pyt"),    # удалить подстроку
    ])
def test_delete_symbol_positive(input_text, symbol, expected_output):
    string = StringUtils()
    assert string.delete_symbol(input_text, symbol) == expected_output


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_text, symbol, expected_output",
    [
        ("Привет", "а", "Привет"),             # удалить несуществующий символ
        ("", "т", ""),                         # удалить символ в пустой строке
        ("hello world", " ", "helloworld"),    # удалить пробел
    ])
def test_delete_symbol_negative(input_text, symbol, expected_output):
    string = StringUtils()
    assert string.delete_symbol(input_text, symbol) == expected_output
