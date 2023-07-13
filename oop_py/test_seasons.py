from seasons import minutes
import pytest

def test_wrong_format():
    with pytest.raises(SystemExit):
        minutes('July 3, 1999')
    with pytest.raises(SystemExit):
        minutes('1999:03:02')
def test_correct_format():
    assert minutes('2023-07-07') == 'One thousand, four hundred forty minutes'
