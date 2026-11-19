from evenodd import num
def test_num():
    result=num(5)
    expected="n=5"
    assert result==expected
def test_num_1():
    result=num(10)
    expected="n_1=10"
    assert result==expected