import pytest
from numb3rs import validate

def test_validate_True():
    assert validate("1.0.100.5") == True
    assert validate("255.06.28.180") == True
    assert validate("10.91.56.165") == True

def test_validate_False():
    assert validate("256.0.1.222") == False
    assert validate("278.7.5.2") == False

def test_validate_sysexit():
    with pytest.raises(SystemExit):
        validate("cat")
        validate("...")