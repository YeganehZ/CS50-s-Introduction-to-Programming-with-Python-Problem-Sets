import pytest
from datetime import date
from seasons import numOfMins

def test_seasons():
    assert numOfMins(date(2023,9,27), date.today()) == 1440
    assert numOfMins(date(1991,9,20), date.today()) == 16842240

def test_error():
    with pytest.raises(TypeError):
        numOfMins("January 1, 2023", date.today)
