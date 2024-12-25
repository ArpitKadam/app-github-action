from src.maths_operations import add, sub, mul, div, exp

def test_add():
    assert add(1,5) == 6
    assert add(2,3) == 5
    assert add(0,0) == 0

def test_sub():
    assert sub(5,3) == 2
    assert sub(3,5) == -2
    assert sub(0,0) == 0

def test_mul():
    assert mul(5,3) == 15
    assert mul(3,5) == 15
    assert mul(0,0) == 0

def test_div():
    assert div(10,5) == 2
    assert div(3,5) == 0.6
    assert div(0,0) == 0

def test_exp():
    assert exp(2,3) == 8
    assert exp(0,0) == 0
    assert exp(1,0) == 1