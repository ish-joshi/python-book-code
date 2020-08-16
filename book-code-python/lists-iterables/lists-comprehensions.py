
"""This module shows efficient ways to generate lists for common patterns of data
It is really vital to keep this code to minimal and easy to read. 

This shows some common examples

The way it works is [ some_value for __ in ___] on any for loop
"""

# Common way 🧙‍♀️
zero_to_ten_vals = []
for num in range(11):
    zero_to_ten_vals.append(num)

# List comprehension method ✅
zero_to_ten = [num for num in range(1, 11)]

# Other common examples
even_nums_0_to_10 = [even_num for even_num in range(0, 11, 2)]

squares_of_nums_0_to_10 = [num**2 for num in range(0, 11)]

copy_list = [item for item in zero_to_ten]

# zero_to_ten:               [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_nums_0_to_10:        [0, 2, 4, 6, 8, 10]
# squares_of_nums_0_to_10:  [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# copy_list:                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]





####### Advanced concept!!!
# Keep it to atmost 1 ternary operation otherwise becomes messy
# This is kinda messy so try and use the other tricks    
alternate_negatives = [(-1*val if index%2 == 0 else val) for index, val in enumerate(range(11))]
# alternate_negatives:      [0, 1, -2, 3, -4, 5, -6, 7, -8, 9, -10]