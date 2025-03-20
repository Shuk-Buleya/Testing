import pytest
import source.my_functions as my_functions


def test_add():
    result = my_functions.add( number1=1,number2=2)
    assert result == 3


def test_divide():
    result = my_functions.divide(number1=10,number2=2)
    assert result == 5

def test_divide_by_0():
    with pytest.raises(ValueError):
        my_functions.divide(number1=10,number2=0)