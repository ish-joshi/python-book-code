
def print_item_messy_none(item, item2):

    # This none check may be messy 😫
    if item is None or item2 is None:
        print("Empty")
    else:
        print(str(item))


def print_item_good(item):

    # Good way I guess to write neater code 😛
    if not item or not item2: # we can simplify this 
        # not (item and item2)
        print("Empty")
    else:
        print(str(item))
