

def do_math(operation, *nums):
    """By adding the * in front of nums, any number of arguements can be accepted
    This is really useful, as they are converted to a tuple;

    do_math('multiply', 1,2,3,4,5) -> Operation=multiply, Nums=(1, 2, 3, 4, 5)
    """

    print(f"Operation {operation}, Nums {nums}")

    if operation == 'add':
        return sum(nums)
    elif operation == 'multiply':
        product = 1
        for num in nums:
            product *= num
        return product
    else:
        raise Exception("Invalid operation")


add_nums = do_math('add', 1, 2, 3, 4, 5) # Operation add, Nums (1, 2, 3, 4, 5)
product = do_math('multiply', 1, 2, 3, 4, 5) # Operation multiply, Nums (1, 2, 3, 4, 5)

print(add_nums) # 15
print(product) # 120


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