
import pytest
from utils.math_utils import add_numbers

def test_add_numbers_basic():
    assert add_numbers([1,2,3]) == 6

def test_add_numbers_empty():
    assert add_numbers([]) == 0

def test_add_numbers_type_errors():
    with pytest.raises(TypeError):
        add_numbers('abc')
    with pytest.raises(TypeError):
        add_numbers([1, 'x'])
