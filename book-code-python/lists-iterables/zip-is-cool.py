# If you parallel lists holding information by index, you can certainly use this.

names = "Ishan,Prince,Surayez".split(",")
ages = [21,24,22]

# Print the name and age together

# Basic approach
for i in range(len(names)):
    name = names[i]
    age = ages[i]
    print(name, age)


# Level up
for name, age in zip(names, ages):
    print(name, age)

# It picks the smaller list :)
# Check out zip_longest if you want the longer one with default values

