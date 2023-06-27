from twttr import shorten
def test_uppercase():
    assert shorten('TWITTER') == 'TWTTR'
    assert shorten('PEOPLE') == 'PPL'
def test_lowercase():
    assert shorten('twitter') == 'twttr'
    assert shorten('people') == 'ppl'
def test_mixedCase():
    assert shorten('TWItter') == 'TWttr'
    assert shorten('peoPLE') == 'pPL'
def test_mixedChars():
    assert shorten('twitter345') == 'twttr345'
    assert shorten('45 people') == '45 ppl'
