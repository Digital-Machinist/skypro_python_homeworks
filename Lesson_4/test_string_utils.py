import pytest # type: ignore
from string_utils import StringUtils

string_utils = StringUtils()

# capitalize func
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

# trim func
@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("    Skypro", "Skypro"),
    (" Hello world", "Hello world"),
    ("                                  Python", "Python"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    (" ^*&^%$^", "^*&^%$^"),
    ("", ""),
    ("   ", "")
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected

# contains func
@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "S", True),
    ("Hello, World!", "d", True),
    ("1234567890", "4", True),
    ("`~!@#$%^&*()_+", "&", True),
    ("Hello, World!", "w", False)
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    #проверка только пробела
    (" ", " ", True),
    #проверка пустой строки
    ("", "", True),
    #проверка поиска символов на разных языках
    ("Symbоl", "o", False),
    #проверка поиска символа из 2х знаков
    ("`~!@#$%^&*()_+", "`~", True)
])
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected

# delete symbol func
@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "S", "kyPro"),
    ("Hello, World!", "!", "Hello, World"),
    ("1234567890", "456", "1237890"),
    ("Hello, 12345!", "12", "Hello, 345!"),
    ("Hello, World!", "Hello, World!", "")
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    #проверка удаления только пробела
    (" ", " ", ""),
    #проверка удаления пустой строки
    (" ", "", " "),
    #проверка удаления подложенного символа на другом языке
    ("Symbоl", "o", "Symbоl")
])
def test_delete_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected