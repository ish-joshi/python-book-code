# List Comprehensions

List comprehension is a shorter way to create a Python list without using loops. 

We can work through common examples:

### List of number range

```python3
# Common way 🧙‍♀️
zero_to_ten = []
for num in range(11):
    zero_to_ten.append(num)
print(zero_to_ten)
```

Instead of the loop, let's look at the comprehension method. 

```python3
# List comprehension method ✅
zero_to_ten = [num for num in range(1, 11)]
print(zero_to_ten)
```

### Even numbers from 0-10
```python3
even_nums_0_to_10 = [even_num for even_num in range(0, 11, 2)]
print(even_nums_0_to_10)
```

### Squares of numbers 0-10
```python3
squares_of_nums_0_to_10 = [num**2 for num in range(0, 11)]
print(squares_of_nums_0_to_10)
```
Notice you can add any python expresson before the `for`. In the above example note `num**2`. 


>💡 Tip: You can also call other methods or construct other classes.

### List Copy
```python3
names = ["adam", "bob", "chrissy", "daisy"]
# Create a non-reference copy of the list
copy_list = [item for item in names]
print(copy_list)
print(hex(id(names)), hex(id(copy_list))) # They are different copies
```

>⚠️ Note: `copy_list = names` only copies the reference and is not the same as creating a new list. 



