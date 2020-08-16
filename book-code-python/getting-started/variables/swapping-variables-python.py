a = 1
b = 2


# Swap two variables ❌
c = a
a = b
b = c

print (a, b)



# Do it this way ✅
a, b = b, a


# What if you want to swap three variables
# a with c, b with c, c with a

# Magic 🧙‍♀️
a, b, c = b, c, a
