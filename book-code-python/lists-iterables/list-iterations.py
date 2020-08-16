
the_list = [i for i in range(0, 11, 2)]

# 👻could give you nightmares
# 1️⃣value with index
for index in range(len(the_list)):
    value = the_list[index]
    print(value)

# ✅use the loops below if you can
# 2️⃣value with loop # No access to index
for value in the_list:
    print(value)


# 3️⃣print both index and value
for index, value in enumerate(the_list):
    print(index, value)