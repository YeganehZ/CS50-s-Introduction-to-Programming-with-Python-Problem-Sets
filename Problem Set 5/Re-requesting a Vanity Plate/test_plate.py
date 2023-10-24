import pytest
from plates import is_valid

def main():
    test_is_valid_True()
    test_is_valid_False()

def test_is_valid_True():
    assert is_valid("AA") == True
    assert is_valid("AA10") == True
    assert is_valid("AA100") == True
    assert is_valid("AAA222") == True


def test_is_valid_False():
    assert is_valid("AA0") == False
    assert is_valid("A .20") == False
    assert is_valid("AAAA222") == False
    
if __name__=="__main__":
    main()