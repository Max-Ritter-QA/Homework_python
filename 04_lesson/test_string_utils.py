import pytest
from String_Utilis import StringUtils

Res = StringUtils()

@pytest.mark.positive_test
@pytest.mark.parametrize(
    "string, result",
    [
        ("hello", "Hello"),
        ("hola123", "Hola123"),
        ("hellow kitty", "Hellow kitty"),
    ])
def test_capitilize_positive(string, result):
    res = StringUtils()
    assert res.capitilize(string) == result

@pytest.mark.negative_test
@pytest.mark.parametrize(
    "string, result",
    [
        (" ", "введите текст"),
        ("", "введите текст"),
        ("123", "введите текст"),
    ])
@pytest.mark.xfail
def test_capitilize_negative(string, result):
    res = StringUtils()
    assert res.capitilize(string) == result


@pytest.mark.positive_test
@pytest.mark.parametrize(
    "string, result",
    [
        (" Laptop is grey", "Laptop is grey"),
        ("   window", "window"),
        (" 123", "123"),
        (' ♦,♣,♠', '♦,♣,♠')
    ])
def test_trim_positive(string, result):
    res = StringUtils()
    assert res.trim(string) == result

@pytest.mark.negative_test
@pytest.mark.parametrize(
    "string, result",
    [
        (" ", "введите текст"),
    ])
@pytest.mark.xfail
def test_trim_negative(string, result):
    res = StringUtils()
    assert res.trim(string) == result


@pytest.mark.positive_test
@pytest.mark.parametrize('string, result', [
     ('1,2,3,4',  ['1', '2', '3', '4']),
     ('a,b,c,d', ['a', 'b', 'c', 'd']),
     ('a,3,5', ['a', '3', '5']),
     ('♦,♣,♠', ['♦', '♣', '♠'])
     ])
def test_to_list_positive(string, result):
    res = StringUtils()
    assert res.to_list(string) == result

@pytest.mark.negative_test
@pytest.mark.parametrize('string, result', [
     ('',  "введите текст"),
     (' ', 'введите текст'),
     ])
@pytest.mark.xfail
def test_to_list_negative(string, result):
    res = StringUtils()
    assert res.to_list(string) == result


@pytest.mark.positive_test
@pytest.mark.parametrize(
    "string, delimeter, result",
    [
        ("a!b!c!d", "!", ["a", "b", "c", "d"]),
        ('1&2&3&4', "&", ['1', '2', '3', '4']),
        ('vэ3э5', "э",['v', '3', '5']),
        ('♦.♣.♠', ".", ['♦', '♣', '♠'])
    ])
def test_to_list_2_positive(string, delimeter, result):
    res = StringUtils()
    assert res.to_list(string, delimeter) == result


@pytest.mark.positive_test
@pytest.mark.parametrize(
    "string, symbol",
    [
        ("Hellow", "w"),
        ("12345", "4" ),
        ('♦♣♠', "♦"),
        ("4VcdЫ", "Ы")
    ])
def test_contains_positive(string, symbol):
    res = StringUtils()
    assert res.contains(string, symbol) == True

@pytest.mark.negative_test
@pytest.mark.parametrize(
    "string, symbol",
    [
        ("Hellow", "q"),
        ("12345", "8" ),
        ('♦♣♠', "!"),
        ("4VcdЫ", "Э")
    ])
@pytest.mark.xfail
def test_contains_negative(string, symbol):
    res = StringUtils()
    assert res.contains(string, symbol) == True


@pytest.mark.positive_test
@pytest.mark.parametrize(
    "string, symbol, result",
    [
        ("Assurance", "s", "Aurance"),
        ("Quality", "ality", "Qu"),
        ("SkyPro", "Sky", "Pro"),
        ("11234", "1", "234"),
        ("Представление", "е", "Прдставлни")
    ])
def test_delete_symbol_positive(string, symbol, result):
    res = StringUtils()
    assert res.delete_symbol(string, symbol) == result

@pytest.mark.negative_test
@pytest.mark.parametrize(
    "string, symbol, result",
    [
        ("Assurance", "s", "Asurance"),
        ("Quality", "perv", "данных символов нет в тексте"),
        ("11234", "6", "данного символа нет в тексте"),
    ])
@pytest.mark.xfail
def test_delete_symbol_negative(string, symbol, result):
    res = StringUtils()
    assert res.delete_symbol(string, symbol) == result


@pytest.mark.positive_test
@pytest.mark.parametrize(
    "string, symbol",
    [
        ("Hellow", "H"),
        ("12345", "1"),
        ("Манго", "М"),
        ("iphone", "i")
    ])
def test_starts_with_positive(string, symbol):
    res = StringUtils()
    assert res.starts_with(string, symbol) == True

@pytest.mark.negative_test
@pytest.mark.parametrize(
    "string, symbol",
    [
        ("Hellow", "w"),
        ("12345", "8"),
        ("Манго", "м"),
        ("iphone", "E")
    ])
@pytest.mark.xfail
def test_starts_with_negative(string, symbol):
    res = StringUtils()
    assert res.starts_with(string, symbol) == True


@pytest.mark.positive_test
@pytest.mark.parametrize(
    "string, symbol",
    [
        ("Hellow", "w"),
        ("12345", "5"),
        ("Манго", "о"),
        ("iphone", "e")
    ])
def test_end_with_positive(string, symbol):
    res = StringUtils()
    assert res.end_with(string, symbol) == True

@pytest.mark.negative_test
@pytest.mark.parametrize(
    "string, symbol",
    [
        ("Hellow", "H"),
        ("12345", "1"),
        ("Манго", "Ж"),
        ("iphone", "h")
    ])
@pytest.mark.xfail
def test_end_with_negative(string, symbol):
    res = StringUtils()
    assert res.end_with(string, symbol) == True


@pytest.mark.positive_test
@pytest.mark.parametrize(
    "string",
    [
        (""),
        ("  "),
        ("                 ")
    ])
def test_is_empty_positive(string):
    res = StringUtils()
    assert res.is_empty(string) == True

@pytest.mark.negative_test
@pytest.mark.parametrize(
    "string",
    [
        ("s"),
        (" ssss"),
        ("     hi world            ")
    ])
@pytest.mark.xfail
def test_is_empty_negative(string):
    res = StringUtils()
    assert res.is_empty(string) == True


@pytest.mark.positive_test
@pytest.mark.parametrize(
    "string, joiner, result",
    [
        (["a", "b", "c", "d"], "!", "a!b!c!d"),
        (['1','2','3','4'], "&", '1&2&3&4'),
        (['a', '3', '5'], "э", 'aэ3э5'),
        (['♦', '♣', '♠'], "5", '♦5♣5♠')
    ])
def test_list_to_string_positive(string, joiner, result):
    res = StringUtils()
    assert res.list_to_string(string, joiner) == result

@pytest.mark.positive_test
@pytest.mark.parametrize('string, result', [
     (['1','2','3','4'], '1,2,3,4'),
     (['a', 'b', 'c', 'd'], 'a,b,c,d'),
     (['a', '3', '5'], 'a,3,5'),
     (['♦', '♣', '♠'], '♦,♣,♠')
     ])
def test_list_to_string_2_positive(string, result):
    res = StringUtils()
    assert res.list_to_string(string) == result

@pytest.mark.negative_test
@pytest.mark.parametrize('string, result', [
     ([], "введите список"),
     ])
@pytest.mark.xfail
def test_list_to_string_2_negative(string, result):
    res = StringUtils()
    assert res.list_to_string(string) == result
