
# Extract the coordinates into x and y variables
coordinates = (0, 1) # x = 0, y = 1

# Messy Method 😱
x = coordinates[0]
y = coordinates[1]


# Neat trick 😄
x, y = coordinates


person_info = ['Name', 18, 'Address is here', '+61422222222']

# Don't do this ❌
name = person_info[0]
age = person_info[1]
# ...

# Do this instead ✅
name, age, address, phone = person_info
# Trust me this works
