from src.strings import *


def test_are_reverses():
    assert are_reverses("abc", "cba") == True
    assert are_reverses("hello", "olleh") == True
    assert are_reverses("Python", "nohtyP") == True
    assert are_reverses("abc", "abc") == False
    assert are_reverses("abc", "abcd") == False
    assert are_reverses("", "") == True
    assert are_reverses("a", "b") == False

def test_contains_double_space():
    assert contains_double_space("This  is a test.") == True
    assert contains_double_space("No double spaces here.") == False
    assert contains_double_space("  Leading double space.") == True
    assert contains_double_space("Trailing space.  ") == True
    assert contains_double_space(" ") == False
    assert contains_double_space("") == False
    assert contains_double_space("Multiple  spaces  inside.") == True
