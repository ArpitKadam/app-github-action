from src.maths_operations import add, sub 

def test_add():
    assert add(1,5) == 6
    assert add(2,3) == 5
    assert add(0,0) == 0

def test_sub():
    assert sub(5,3) == 2
    assert sub(3,5) == -2
    assert sub(0,0) == 0