from collections import defaultdict
from collections import deque


def two_sum(nums, target):
    """Given an array of integers, return indices of the two numbers such that
    they add up to a specific target.

    Args:
        nums (list): The list of integers to scan.
        target (int): The target.

    Returns:
        (list) The indexes of the elements that sum to the target value.
    """
    # convert `target` to dictionary for fast search
    numbers = defaultdict(deque)
    for idx, number in enumerate(nums):
        numbers[number].append(idx)

    # find complement number to sum up to target
    for first_num in nums:
        complement_num = target - first_num
        if complement_num in numbers:
            if complement_num == first_num and len(numbers[first_num]) < 2:
                continue
            first_idx = numbers[first_num].popleft()
            second_idx = numbers[complement_num].popleft()
            return [first_idx, second_idx]

