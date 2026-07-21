

def is_isomorphic(s: str, t: str) -> bool:
    # Determine whether characters in one strin can map consistently to characters in another
    if len(s) != len(t):
        return False

    s_count = {}
    t_count = {}
    for i in range(len(t)):
        s_count[s[i]] = s_count.get(s[i], 0) + 1
        t_count[t[i]] = t_count.get(t[i], 0) + 1
        if (t_count[t[i]] != s_count[s[i]]):
            return False
    return True


def word_pattern(pattern: str, sentence: str) -> bool:
    words = sentence.split(" ")
    if len(words) != len(pattern):
        return False

    word_to_char = {}
    char_to_word = {}

    for char, word in zip(pattern, words):
        if word in word_to_char and word_to_char[word] != char:
            return False
        if char in char_to_word and char_to_word[char] != word:
            return False

    return True


def group_anagrams(words: list[str]) -> list[list[str]]:
    anagrams = {}
    for word in words:
        char_frequency = [0] * 26
        for char in word:
            index = ord(char) - ord('a')
            char_frequency[index] += 1
        keys = tuple(char_frequency)
        if keys not in anagrams:
            anagrams[keys] = []
        anagrams[keys].append(word)

    return list(anagrams.values())


"""
So what did I learn/practice:

I remembered that in python you can get the ascii value of a value with the ord() function (ord('a') is 97).
I remembered that to insert a value into the end of a list in python you use .append.
I remembered that in python keys in dictionaries must be hashable and therefore imutable data types such as strings or tuples.
I learned that you can use the list() function to create a list of some data. Here I use list() to create a list storing each value in the hashmap.
I remembered that you create a list of length n with [0] * n.
"""
