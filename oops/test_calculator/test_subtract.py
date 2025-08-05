from calculator import subtract

def test_subtract():
    assert subtract(2, 2) ==  0
    assert subtract(6, 2) ==  4
    assert subtract(5, 3) ==  2