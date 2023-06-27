from plates import is_valid

def test_plateLength():
  assert is_valid('K') == False
  assert is_valid('KD234KFJG') == False

def test_firstTwo():
    assert is_valid('23KSF') == False
    assert is_valid('K2DFGR') == False

def test_firstDigit():
    assert is_valid('KD0234') == False

def test_alnum():
    assert is_valid('KD#02') == False
def test_valid():
    assert is_valid('CS50') == True
    
