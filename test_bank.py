from bank import value

def test_hello():
    assert value('hello') == '$0'
    assert value('HELLO') == '$0'
def test_h():
    assert value('hi') == '$20'
    assert value('HI') == '$20'
def test_noH():
    assert value('what?') == '$100'
    assert value('WHAT?') == '$100'
