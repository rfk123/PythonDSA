
# A file for improving at hashmaps and sets in python
# Purpose of using a set in DSA is to remember if something exists
# Purpose of using a map in DSA is to remember information attached to something

# Sets in python
# A set stores only unique values
seen = set()
seen.add(4)
seen.add(5)
seen.add(4)
# seen looks like {4, 5}

# The main purpose of using a set is for quick lookup (O(1) average)

# A hashmap (also called a dictionary in python) stores key-value pairs
# Hashmaps are not only helpful for remembering if something exists but also for remembering things about/attached to the value
"""
Examples
count[num] = frequency
index_by_num[num] = index
last_seen[char] = index
group_by_key[key] = list_of_items
"""


""" Core Operations for both hashmaps and sets """
# Sets
print("Set Prints Incoming")
# you can add to a set using .add()
seen.add(10)
# you can remove a value from a set with .remove()
seen.remove(4)
# However, remove will throw an error if the value doesnt exist
# Instead, you can use discard for the same purpose but minus the error possibility
seen.discard(4)
# You can check if a value is in a set by using the keyword 'in'
print(10 in seen)
# You can find the length of a set using the built-in len function
print(len(seen))
print("Set Prints Finished")

# Hashmaps (dictionaries)
print("Hashmap Prints Incoming")
# You can initialize a hashmap with curly brackets
counts = {}
# You can add to a hashmap using square brackets
counts["a"] = 1
# Note that in this example, "a" is the key and 1 is the value
# In python, keys for hashmaps must be of a hashable data type (which just means it must be immutable)
# You can adjust the value of a key-value pair with square brackets
counts["a"] += 1  # counts["a"] now has the value 2
# One way to see if a hashmap contains a value is to use the 'in' keyword
print("a" in counts)
# To get a value or error if missing you can just use bracket notation
print(counts["a"])
# If you want to get a value from the hashmap and have a default value instead of error if it doesnt exist then uset .get(,)
print(counts.get('A', 0))
# For deleting a value from the hashmap you can use the del keyword
del counts["A"]
# To find the length (size) of a hashmap you can use the built-in len function
print(len(counts))

# Lets use what we have learned to build a hashmap to store characters and their frequencies given a string


def count_frequencies(str):
    counts = {}
    for char in str:
        counts[char] = counts.get(char, 0) + 1
    pass
# This function will create a hashmap that, if 'banana' was inputted, would look like {'b' : 1, 'a' : 3, 'n' : 2}
# What is important to notice about this function is that the .get method does not error if the hashmap does not contain our char
# Instead it gives the default value 0 which is nice to use when trying to count frequencies


""" A Little Bit of Understand On Why Sets and Hashmaps Have Fast Lookups """
# Sets and dictionaries use hashing which means it takes a value and converts it into a hash code.
# Essentially hashing just means that the computer takes the requested key and feeds that key into a hash function which converts the key into a consisten unique integer called a hash code
# Then the computer stores the hashcode within some internal array using a modulo operation hash_code % size_of_array to find an index to store it in.
# since computers can access any index of a standard array instantly via RAM address calculations, the program jumps directly to that percise memory location to retrieve the data
# Learn more on hash collisions to find out what happens when two keys create hashcodes that land the same index.
