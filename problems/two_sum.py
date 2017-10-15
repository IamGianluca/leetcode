from collections import defaultdict
from collections import deque


def two_sum(nums, target):
    """Given an array of integers, return indices of the two numbers such that
    they add up to a specific target.

    Args:
        nums (list): The list of integers to scan.
        target (int): The target.

    Returns:
        (list) The indexes of the elements that sum to the target.
    """
    # use dictionary to search in O(1) complexity
    numbers = defaultdict(deque)
    for idx, number in enumerate(nums):
        numbers[number].append(idx)

    # find complement number to sum up to target
    for first_num in nums:
        complementary_number = target - first_num
        if complementary_number in numbers:
            if complementary_number == first_num:
                if len(numbers[first_num]) < 2:
                    continue
            first_idx = numbers[first_num].popleft()
            second_idx = numbers[complementary_number].popleft()
            return [first_idx, second_idx]

