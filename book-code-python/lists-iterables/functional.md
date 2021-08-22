# Functional Programming in Python


There are three common types of operations with functional programming
* Filter (Keep relevant items only)
* Map (Transformation)
* Reduce (Converge to a value)


## Filter
Let's look at `filter` first to understand how it can be used in Python. 

### Keep only even numbers

First, we will have a look at the loop approach, which is a common way of solving this problem. 

```python
nums = [num for num in range(11)]

def is_even(num):
    return num % 2 == 0

### focus start
all_evens = []
for num in nums:
    if is_even(num):
        all_evens.append(num)
### focus end

print(all_evens)
```

Phew! That's a lot of lines of code. Can we simplify the loop section? Yes we can!.

```python
nums = [num for num in range(11)]

def is_even(num):
    return num % 2 == 0

### focus start
all_evens = list (filter(is_even, nums))
### focus end

print(all_evens)
```

You can also specify your filter function inline using `Lambdas`. 

```python
nums = [num for num in range(11)]
evens_with_lambda = list ( filter(lambda num: num%2 == 0, nums))
print(evens_with_lambda)
```

Each list item, in this case each number is passed into the first parameter of the function specified in filter. 

If that function returns `True` the item is kept, otherwise it is ignored.


## Map
Now, let's look at transforming iterables (lists) in Python. 

If you can write a function to convert a single value, like `calculate_area_from_radius(radius=___)`, this can be easily extended to convert all elements in a list. 

```python
def area(radius):
    return math.pi * (radius**2)

circle_radiuses = [2, 3, 10.5] # radius in cm
areas = []
for radius in circle_radiuses:
    circle_area = area(radius)
    areas.append(circle_area)
print(areas)
```

This can be re-written to use `map`

```python

def area(radius):
    return math.pi * (radius**2)

circle_radiuses = [2, 3, 10.5] # radius in cm
areas = list(map(area, circle_radiuses))
print(areas)

```

## Reduce
Will be updated later...

