import pytest
from working import convert

def test_AMtoAM () :
    assert convert("9:00 AM to 11:15 AM") == "09:00 to 11:15"
    assert convert("9 AM to 11 AM") == "09:00 to 11:00"

def test_AMtoPM():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_PMtoAM():
    assert convert("5:05 PM to 1:05 AM") == "17:05 to 01:05"
    assert convert("5 PM to 1 AM") == "17:00 to 01:00"

def test_PMtoPM():
    assert convert("5:00 PM to 10:30 PM") == "17:00 to 22:30"
    assert convert("5 PM to 10 PM") == "17:00 to 22:00"

def test_convert_sysexit():
    with pytest.raises(SystemExit):
        convert("Hi")
        convert("09:61 AM to 10:30 PM")