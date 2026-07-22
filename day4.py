

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


"""
The information stored in s_count is essentially just a character stored with its frequency count. Same for t_count.
My thought process is that if we itterate through both strings and the current character's frequencies in both s and t differ then we have a mismatch and therefore the strings structures don't map to each other.
The implementation essentially just ensures that the two strings are of the same length, create two hashmaps to store frequency counts for each word, loop through each word and check frequencies to see if there is an early exit, and then once loop done return true.
The time complexity is O(n) because at the worst case we visit each character in both strings but in just one pass so since they are the same size it is O(n).
The space complexity is O(n) because if each character in the strings were unique then the hashmap lengths would match the length of the strings. however there are only 26 possible strings to consider.
test cases could be strings of different sizes, strings like 'aappl' and 'bbllp' (would return true), and 'aaaaa' with 'bbbbb' (would return true)
"""


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


"""
The information stored in word_to_char 
"""


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
I learned that you can use zip(x,y) to loop over both x and y at the same time
"""
