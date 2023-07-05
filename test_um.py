from um import count

def test_um():
    assert count('hello, um, world') == 1
    assert count('hello, um um, world') == 2

def test_word_with_um():
    assert count('yummy') == 0
    assert count('nice umbrella') == 0

def test_uppercase():
    assert count('hello, UM, WORLD') == 1
    assert count('NICE UMBRELLA') == 0
    assert count('Hello, um um, world') == 2