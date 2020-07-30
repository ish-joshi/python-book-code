# Confusing to read ❌
def xor_bad(a, b):
    return (a and (not b)) or (b and (not a))

# Make it easier for yourself 😍
def xor(a, b):
    vals = [a, b]
    # not all and any one = xor
    return (not all(vals)) and any(vals)



# Logic gate with more than two inputs
a, b, c = [True] * 3

# This will drive you insane 🤔
def ok_more_than_two_and(a, b, c):
    return (a and b) and c

def ok_more_than_two_or(a, b, c):
    return (a or b) or c


# Better way for any number of variables ✅
def good_more_than_two_and(a, b, c):
    # Use the all with a list to check if all True
    return all([a, b, c])

def good_more_than_two_or(a, b, c):
    # Use the any with a list to check if any is True
    return any([a, b, c])


