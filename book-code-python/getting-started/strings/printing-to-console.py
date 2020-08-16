
# Print many variables 

age = 21
name = "Ishan"
uni = "Monash"
fees = 500.50
likes = ["Apple"]

print("Age is " + str(age) + ". Name is " + name + " " + uni + " " + str(fees) + " " + str(likes))
# Age is 21. Name is Ishan Monash 500.5 ['Apple']

# This is slightly better
print("Age is {}. Name is {} {} {} {}".format(age, name, uni, fees, likes))


# Try this instead
print(f"Age is {age}. Name is {name} {uni} {fees} {likes}")

