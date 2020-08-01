
def print_item_messy_none(item):

    # This none check may be messy 😫
    if item is None:
        print("Empty")
    else:
        print(str(item))


def print_item_good(item):

    # Good way I guess to write neater code 😛
    if not item:
        print("Empty")
    else:
        print(str(item))
