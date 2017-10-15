from collections import defaultdict


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
    numbers = defaultdict(list)
    for idx, number in enumerate(nums):
        numbers[number].append(idx)

    # TODO: needs refactor
    # find complement number to sum up to target
    for first_num in nums:
        complementary_number = target - first_num
        a = numbers[first_num][0]
        try:
            b = numbers[complementary_number]
        except IndexError:
            pass
        else:
            if first_num == complementary_number:
                idx = 1
            else:
                idx = 0
            try:
                b[idx]
            except IndexError:
                pass
            else:
                return [a, b[idx]]

