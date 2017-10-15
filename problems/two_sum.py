from collections import defaultdict
from collections import deque


def two_sum(nums, target):
    """Given an array of integers, return indices of the two numbers such that
    they add up to a specific target.

    Notes: O(n) time complexity. We traverse the list containing n elements
        exactly twice. Since the hash table reduces the look up time to O(1),
        the time complexity is O(n).

    Args:
        nums (list): The list of integers to scan.
        target (int): The target.

    Returns:
        (list) The indexes of the elements that sum to the target value.
    """
    # convert `target` to dictionary for fast search
    num_to_idx = defaultdict(deque)
    for idx, number in enumerate(nums):
        num_to_idx[number].append(idx)

    # find complement number to sum up to target
    for first_num in nums:
        complement_num = target - first_num
        if complement_num in num_to_idx:
            if complement_num == first_num and len(num_to_idx[first_num]) < 2:
                continue
            first_idx = num_to_idx[first_num].popleft()
            second_idx = num_to_idx[complement_num].popleft()
            return [first_idx, second_idx]

    raise ValueError('No two sum solution.')

