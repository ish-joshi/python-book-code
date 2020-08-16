
from collections import Counter, defaultdict


def count_chars(word):
    counting = {}
    for letter in word:
        if counting.get(letter) is None:
            counting[letter] = 0
        counting[letter] += 1
    print(counting)


# We can simplify this a bit 
def counting_with_default_dict(word):
    counting = defaultdict(int)
    for letter in word:
        # this will never be none because defaultdict
        counting[letter] += 1
    print(counting)


# Let's do a two liner
def counting_magic(word):
    counting = Counter(word)
    print(counting)



word = "ishan"
count_chars(word)
counting_with_default_dict(word)
counting_magic(word)

# {'i': 1, 's': 1, 'h': 1, 'a': 1, 'n': 1}
# defaultdict(<class 'int'>, {'i': 1, 's': 1, 'h': 1, 'a': 1, 'n': 1})
# Counter({'i': 1, 's': 1, 'h': 1, 'a': 1, 'n': 1})


        



