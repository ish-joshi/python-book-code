
# is does not replace the == sign
"""
`is` refers to the direct memory location of the variable
whereas the == operator checks if the values are equal
"""


# Maybe you expected this 🤫
x = [1,2]
y = [1,2]

print (x == y) # True
print (x is y) # False

"""
Memory Diagram

[ - | X | - | Y | - ] # Memory
[ 0 | 1 | 2 | 3 | 4 ] # Address

"""


# This will baffle you now 😱
a = [1,2]
b = a

print (a == b) # True
print (a is b) # True

"""
Memory diagram

[ - |  AB  | - | - | - ] # Memory
[ 0 |  1   | 2 | 3 | 4 ] # Address
"""