
from typing import List


# Create pairs and return list
# [1, 2, 6, 7, 9] --> [(1, 2), (2, 6), (6, 7), (7, 9)]
def bad_make_pairs(nums: List[int]) -> List[tuple]:
    out = []
    for i in range(len(nums) - 1):
        to_add = (nums[i], nums[i+1])
        out.append(to_add)
    return out


def good_make_pairs(nums: List[int]) -> List[tuple]:
    assert len(nums) > 1
    return list ( zip(nums, nums[1:]))





# Find the biggest difference between adjacent elements

diff = -10000000 # really small num

def find_largest_adjacent_difference(nums: List[int]) -> int:
    """This functions checks the difference of all the adjacent elements and returns the largest difference

    [1, 2, 6, 7, 9]
    (2-1) = 1
    (6-2) = 4
    (7-6) = 1
    (9-7) = 2

    Returns 4

    Args:
        nums (List[int]): list of numbers

    Returns:
        int: the largest difference
    """
    pass


