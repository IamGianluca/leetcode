from collections import defaultdict
from collections import deque


def two_sum(nums, target):
    """Given an array of integers, return indices of the two numbers such that
    they add up to a specific target.

    Notes: O(n) time complexity. We traverse the list containing n elements
        only once. Each look up in the table costs only O(1) time.

    Args:
        nums (list): The list of integers to scan.
        target (int): The target.

    Returns:
        (list) The indexes of the elements that sum to the target value.
    """
    # convert `target` to dictionary to loop up in O(1) time
    num_to_idx = defaultdict(deque)

    for idx, number in enumerate(nums):
        complement_num = target - number
        if complement_num in num_to_idx:
            first_idx = num_to_idx[complement_num].popleft()
            return [first_idx, idx]

        # add to dictionary for future search
        num_to_idx[number].append(idx)

    raise ValueError('No two sum solution.')

