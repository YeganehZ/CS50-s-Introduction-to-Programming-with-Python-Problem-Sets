import pytest
from twttr import shorten

     
def test_vowels():
    assert shorten("hello") == "hll" 
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("Yeganeh") == "Ygnh"
    assert shorten("Hello, World!") == "Hll, Wrld!"
    assert shorten("23")== "23"
    assert shorten(".") == "." 


