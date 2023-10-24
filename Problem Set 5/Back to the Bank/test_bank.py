import pytest 
from bank import value

def main():
    test_value_zero()
    test_value_20()
    test_value_100()

def test_value_zero():
    assert value("hello") == 0
    assert value("HeLLo") == 0
    assert value("HELLO, Yeganeh") == 0
    


def test_value_20():
    assert value("Hey") == 20
    assert value("HI") == 20 

def test_value_100():
    assert value("greetings Yeganeh") == 100
    assert value("   greetings Yeganeh  ") == 100

if __name__=="__main__":
    main()