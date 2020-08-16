
# Sometimes you have to accept coordinates as params

######################################### Helper
def distance_from_origin(x0, y0):
    return sqrt(x0**2 + y0**2)



point = (9, 10)

# Why not simplify this? 🤔
x,y = point
dist = distance_from_origin(x, y)


# Unpacking, the good way ✅
dist = distance_from_origin(*point)

# The * unpacks the point tuple and distributes it to the parameters
# point[0] = the first parameter which is x0
# point[1] = the second parameter which is y0






import random
# these are 10 randomly generated points 
points = [(random.randint(0, 10), random.random(0, 10)) for _ in range(10)]
# we want to convert to an array of distances from origin

#########################################


# Why not simplify it? 🤔
dists = []
for point in points:
    x, y = point
    dist = distance_from_origin(x, y)
    dists.append(dist)


# Good way ✅
dists = []
for point in points:
    dist = distance_from_origin(*point)
    # The * unpacks the point tuple and distributes it to the parameters
    # point[0] = the first parameter which is x0
    # point[1] = the second parameter which is y0
    dists.append(dist)


