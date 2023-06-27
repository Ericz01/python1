from fuel import convert, gauge
import pytest

def test_int_conversion():
    assert convert('3/4') == 75
    assert convert('2/4') == 50
def test_empty():
    assert gauge(0) == 'E'
    assert gauge(1) == 'E'
def test_full():
    assert gauge(100) == 'F'
    assert gauge(99) == 'F' 
def test_percentage():
    assert gauge(50) == '50%'
    assert gauge(35) == '35%'
def test_ValueError():
    with pytest.raises(ValueError):
        convert('cow/cat')
def test_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        convert(1/0)
        
