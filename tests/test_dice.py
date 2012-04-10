from nose.tools import *
from mock import Mock, patch

from pk.dice import D8, D12p1

@patch('pk.dice.random')
def test_normal_D8(mock_random):
    mock_random.randint.return_value = 5
    r = D8.roll()
    assert_equals(r, 5)

@patch('pk.dice.random')
def test_normal_D12p1(mock_random):
    mock_random.randint.return_value = 1
    r = D12p1.roll()
    assert_equals(r, 2)

@patch('pk.dice.random')
def test_limit_D12p1(mock_random):
    mock_random.randint.return_value = 12
    r = D12p1.roll()
    assert_equals(r, 12)
