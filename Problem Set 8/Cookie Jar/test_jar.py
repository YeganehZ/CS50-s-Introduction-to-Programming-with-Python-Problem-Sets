import pytest
from jar import Jar

def test_str():
    jar=Jar()
    assert str(jar)=="🍪🍪🍪🍪"
    jar.deposit(1)
    assert str(jar)=="🍪🍪🍪🍪🍪"
    jar.deposit(3)
    assert str(jar)=="🍪🍪🍪🍪🍪🍪🍪🍪"
    jar.withdraw(4)
    assert str(jar)=="🍪🍪🍪🍪"

def test_init():
    jar=Jar()
    assert jar.capacity == 12
    jar2=Jar(3)
    assert jar2.capacity == 3

def test_deposit():
    jar=Jar()
    assert jar.deposit(3)=="🍪🍪🍪🍪🍪🍪🍪"
    assert jar.deposit(4)=="🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_withdraw():
    jar=Jar()
    jar.deposit(3)
    assert jar.withdraw(2)=="🍪🍪🍪🍪🍪"    
    assert jar.withdraw(1)=="🍪🍪🍪🍪"
    assert jar.size == 4

def test_error():
    with pytest.raises(ValueError):
        jar=Jar("1")
    
    with pytest.raises(ValueError):
        jar=Jar()
        jar.deposit(14)

  
    with pytest.raises(ValueError):
        jar=Jar()
        jar.deposit(5)
        jar.withdraw(10)


