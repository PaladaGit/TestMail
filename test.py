import pytest

def concStr(s1,s2):
    return s1 + s2
# test 1 for str
def test_StrConc():
    assert concStr("1","2") == "12"


def countStr(s1,s2):
    return s1.count(s2)
# test 2 for str
@pytest.mark.parametrize("test_s2, ExpR", [("0",5), ("",12), ("5",0),("1232100000",0)])  
def test_countStr(test_s2,ExpR):
    assert countStr("12321 00000",test_s2) == ExpR
    
# test 3 for str
def test_compareStr():
    a = 100
    b = "100"
    try:
    	assert a == b
    except AssertionError: 
    	pass


def tupleSum(t1):
    return sum(t1)
# test 1 for tuple
def test_TupleSum():
    p_tup = (1, 1, 123, 11)
    assert tupleSum(p_tup) == 136

# test 2 for tuple
@pytest.mark.parametrize("test_input", [(1, "2"), (1, True), (1, 'Do')])    	
def test_IncorrectTupleSum(test_input):
    try:
    	assert tupleSum(test_input)
    except TypeError:
    	pass

# test 3 for tuple
def tupleCount(t1,s1):
    return t1.count(s1)
def test_tupleCount():
    p_tup = ("1", 1, "123", 11, True)
    assert tupleCount(p_tup,"1") == 1
