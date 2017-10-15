from collections import defaultdict
from collections import deque


def two_sum(numbers, target):
    """Given an array of integers, return indices of the two numbers such that
    they add up to a specific target.

    Notes: O(n) time complexity. We traverse the list containing n elements
        only once. Each look up in the table costs only O(1) time.

    Args:
        numbers (list): The list of integers to scan.
        target (int): The target.

    Returns:
        (list) The indexes of the elements that sum to the target value.
    """
    already_seen = defaultdict(deque)
    for idx, number in enumerate(numbers):
        complement = target - number
        if complement in already_seen:
            complement_idx = already_seen[complement].popleft()
            return [complement_idx, idx]
        already_seen[number].append(idx)
    raise ValueError('No solution found')

