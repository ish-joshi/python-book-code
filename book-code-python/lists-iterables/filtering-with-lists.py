
nums = [num for num in range(11)]

def is_even(num):
    return num % 2 == 0


all_evens_long = []
for num in nums:
    if is_even(num):
        all_evens_long.append(num)
print(all_evens_long)





all_evens = list ( filter(is_even, nums))

evens_with_lambda = list ( filter( lambda num: num%2 == 0, nums))


def divisible_by_three(num):
    return num % 3 == 0

all_divisible_by_three = list ( filter(divisible_by_three, nums))


# Works with strings as well

names = ['Prince', 'Ishan', 'Surayez', 'Lim', 'Snake', 'Cam', 'Yen']

def name_is_five_chars_long(name):
    return len(name) == 5

all_names_5_long = list ( filter(name_is_five_chars_long, names))
# ['Ishan', 'Snake']


# Filter basically takes a function that takes any parameter and returns a boolean.
