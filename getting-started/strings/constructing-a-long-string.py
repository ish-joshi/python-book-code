

names = ['Prince', 'Ishan', 'Surayez', 'Lim', 'Snake', 'Cam', 'Yen']


# Convert to a string with one name on each line

# This is inefficient 😢
out = ""
for name in names:
    out += (name + "\n")
print(out)


# Try this instead 😌
out = "\n".join(names)

