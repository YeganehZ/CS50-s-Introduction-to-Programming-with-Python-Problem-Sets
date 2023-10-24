import pytest
from um import count

def test_count_zero():
    
    assert count("hi, world.") == 0 
    assert count("yummy") == 0
    assert count("yum") == 0


def test_count_one():

    assert count("Hello, um, world.") == 1
    assert count("hi, Um, world.") == 1
    assert count("um...") == 1

def test_count_two():
    assert count("um, hi, um, world.") == 2
    assert count("hi, um, UM, world") == 2
