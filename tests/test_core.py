# tests/test_core.py

import pytest
from grapes_tokenizer.core import GrapesTokenizer

@pytest.mark.parametrize("text, expected", [
    ("a", 1),                               # single letter
    ("abc", 1 + 2 + 3),                    # simple letters sum
    ("xyz", 24 + 25 + 26),                 # end of alphabet
    ("Hello", 8 + 5 + 12 + 12 + 15),       # case-insensitive letters
])
def test_simple_letters(text, expected):
    tok = GrapesTokenizer(positional=False, case_sensitive=False)
    assert tok.encode(text) == expected


def test_digits_mapping():
    tok = GrapesTokenizer()
    # '0'->0, '5'->5, '9'->9
    assert tok.encode("059") == 0 + 5 + 9


def test_specials_mapping():
    tok = GrapesTokenizer()
    # space=32, '!'=33, '@'=64
    assert tok.encode(" !@") == 32 + 33 + 64


def test_mixed_characters():
    tok = GrapesTokenizer()
    # "a1!b" -> a=1 + '1'=1 + '!'=33 + b=2 = 37
    assert tok.encode("a1!b") == 1 + 1 + 33 + 2


def test_positional_with_digits_specials():
    tok = GrapesTokenizer(positional=True)
    # "A1!" -> A(=1*1) + '1'(=1*2) + '!'(=33*3) = 1 + 2 + 99 = 102
    assert tok.encode("A1!") == 1 + 2 + 99


def test_empty_string():
    tok = GrapesTokenizer()
    assert tok.encode("") == 0


def test_long_text_performance():
    # a mix of printable ASCII characters repeated
    long_text = "".join(chr((i % 94) + 33) for i in range(1000))
    tok = GrapesTokenizer()
    result = tok.encode(long_text)
    assert isinstance(result, int)
    assert result > 0
