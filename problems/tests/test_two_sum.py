import pytest
from pytest import raises

from problems.two_sum import two_sum


@pytest.mark.parametrize('numbers,target,expected', [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([11, 15, 2, 7], 9, [2, 3]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
    ([-3, 4, 3, 90], 0, [0, 2]),
    ([5, 75, 25], 100, [1, 2]),
    ([5, 5, 5], 10, [0, 1])
])
def test_two_sum(numbers, target, expected):
    assert two_sum(numbers=numbers, target=target) == expected

def test_two_sum_error():
    with pytest.raises(ValueError):
        two_sum(numbers=[1, 1, 5], target=10)

