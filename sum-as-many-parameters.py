
# Accepting as many parameters as you want

def sum_it(*nums):
    added = 0
    for num in nums:
        added += num
    return added


if __name__ == "__main__":
    """Multiple parameters are used and it works!
    """
    sum_it(1,2) # 3
    sum_it(1,2,3,4,5) # 15
