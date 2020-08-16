# Lambdas are just functions in one line. 


def is_even(number):
    return number%2 == 0


is_even_lambda = lambda num: num % 2 == 0


# Both have the same result

print(is_even(4))
print(is_even_lambda(4))