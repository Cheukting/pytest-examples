from unittest import mock
from b import some_func

@mock.patch('a.SomeClass')
def test_some_func(mock_func):
    some_func()
    assert False