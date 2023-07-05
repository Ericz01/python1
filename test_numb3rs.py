from numb3rs import validate

def test_all_numbers():
    assert validate('22.34.16.45') == True
    assert validate('foo.bar.invalid') == False
    assert validate('22..245..233.4') == False
def test_numbers_below_256():
    assert validate('256.245.254.234') == False
    assert validate('245.13.270.275') == False
    assert validate('0.0.1.1') == True

def test_format():
    assert validate('23 23 23') == False
    assert validate('34.23:24.30') == False

def test_more_4_segments():
    assert validate('234.43.29') == False
    assert validate('234.5.5.32') == True