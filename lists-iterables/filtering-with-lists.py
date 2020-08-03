
nums = [num for num in range(11)]


def is_even(num: int) -> bool:
    return num % 2 == 0

all_evens = list ( filter(is_even, nums))


def divisible_by_three(num: int) -> bool:
    return num % 3 == 0

all_divisible_by_three = list ( filter(divisible_by_three, nums))


# Works with strings as well

names = ['Prince', 'Ishan', 'Surayez', 'Lim', 'Snake', 'Cam', 'Yen']

def name_is_five_chars_long(name: str) -> bool:
    return len(name) == 5

all_names_5_long = list ( filter(name_is_five_chars_long, names))
# ['Ishan', 'Snake']
