"""A common approach is where the values of a list need to be transformed.
This section shows how to avoid using loops to get more readable code
"""

nums_zero_to_10 = [num for num in range(11)]

# Convert to a list of True and False indicating even or not.

def is_even(n):
    return n % 2 == 0

# Don't do this ❌
output = []
for num in nums_zero_to_10:
    if is_even(num):
        output.append(True)
    else:
        output.append(False)
    # Could be simplified to 
    # output.append(is_even(num))



# Does this fit better 😌
evens_or_not = list ( map(is_even, nums_zero_to_10))


# Other examples

def double(n):
    return n * 2

double_them_all = list ( map(double, nums_zero_to_10))


def two_raised_to_n(n):
    return 2**n

powers_of_two = list ( map(two_raised_to_n, nums_zero_to_10))


# Note you can also use a lambda function here. 
