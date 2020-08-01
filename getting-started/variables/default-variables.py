

def create_list(size, with_value = 0):
    """Shows how to use the default paramter for with_value

    Args:
        size (int): the size of the list
        with_value (int, optional): the fill value of list. Defaults to 0.

    Returns:
        List[int]: a list of 'with_value'
    """
    return [with_value] * size

# Notice it defaults to 0 if no second parameter is provided

zeroes = create_list(10)
ones = create_list(10, 1)

print(zeroes) # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print(ones) # [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
