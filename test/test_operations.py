from src.maths_operations import add, sub 

def test_add():
    assert add(1, 2) == 3

def test_sub():
    assert sub(2, 1) == 1

def test_mul():
    assert mul(2, 3) == 6

def test_div():
    assert div(6, 2) == 3

def test_mod():
    assert mod(5, 2) == 1