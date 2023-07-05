import pytest
from working2 import convert

def test_format1():
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
    assert convert('8 PM to 8 AM') == '20:00 to 08:00'
    assert convert('12 PM to 12 AM') == '12:00 to 00:00'

def test_format2():
    assert convert('9:00 AM to 5:00 PM') == '09:00 to 17:00'
    assert convert('8:00 PM to 8:00 AM') == '20:00 to 08:00'
    assert convert('12:00 PM to 12:00 AM') == '12:00 to 00:00'

def test_minute_limits():
    with pytest.raises(ValueError):
        convert('4: 00 PM to 8:99 AM')

def test_hour_limit():
    with pytest.raises(ValueError):
        convert('16 PM to 18 PM')

def test_wrong_format2():
    with pytest.raises(ValueError):
        convert('9:00 PM - 5:00 PM')
