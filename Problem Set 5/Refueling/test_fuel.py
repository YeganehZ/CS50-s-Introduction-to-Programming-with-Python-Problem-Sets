import pytest
from fuel import convert 
from fuel import gauge

def main():
    test_convert()
    test_guage()
    test_zero_division()
    test_value()

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_value():
    with pytest.raises(ValueError):
        convert("2/1") 
        convert("cat/dog")   
    

def test_convert():
    assert convert("1/2")==50
    assert convert("99/100")== 99
    assert convert("1/100")== 1
    assert convert("2/3")== 67

    


def test_guage():
    assert gauge(50)== "50%"
    assert gauge(99)== "F"
    assert gauge(1)== "E"
    assert gauge(67)== "67%"  

  
    
if __name__=="__main__":
    main()