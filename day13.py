
# Write this function from memory
def longest_two_distinct(s: str) -> int:
    """
    Return the length of the longest contiguous substring
    containing at most two distinct characters.
    """
    char_counts = {}
    left = 0
    right = 0
    max_length = 0

    while right < len(s):
        char_counts[s[right]] = char_counts.get(s[right], 0) + 1
        while len(char_counts) > 2:
            char_counts[s[left]] -= 1
            if char_counts[s[left]] == 0:
                del char_counts[s[left]]
            left += 1
        max_length = max(max_length, right - left + 1)
        right += 1

    return max_length


# print(longest_two_distinct("eceba"))   # 3, from "ece"
# print(longest_two_distinct("ccaabbb"))  # 5, from "aabbb"
# print(longest_two_distinct(""))        # 0
# print(longest_two_distinct("aaaa"))    # 4


"""
| `right` | Incoming | Counts after adding | Shrinking performed | `left` after shrinking | Valid window | Maximum |
| ------: | -------- | ------------------- | ------------------- | ---------------------: | ------------ | ------: |
|       0 | `"e"`    |  {'e': 1}           | -                   | 0                      | 'e'          | 1       |
|       1 | `"c"`    |  {'e':1, 'c':1}     | -                   | 0                      | 'ec'         | 2       |
|       2 | `"e"`    |  {'e':2, 'c':1}     | -                   | 0                      | 'ece'        | 3       |
|       3 | `"b"`    |  {'e':2, 'c':1, 'b':1}| removed e then c  | 2                      | 'eb'         | 3       |
|       4 | `"a"`    |  {'e':1, 'b':1, 'a':1}| removed e         | 3                      | 'ba'         | 3       |

Time complexity: O(n)
Space Complexity: O(n)
Why delete zero frequency key: We delete that entry in our dictionary when its value hits 0 because that means we no longer have that character in our window.
"""


def longest_k_distinct(s: str, k: int) -> int:
    """
    Return the length of the longest contiguous substring
    containing at most k distinct characters.
    """
    counts = {}
    left = 0
    right = 0
    max_length = 0

    if k <= 0:
        return 0

    while right < len(s):
        counts[s[right]] = counts.get(s[right], 0) + 1
        while len(counts) > k:
            counts[s[left]] -= 1
            if counts[s[left]] == 0:
                del counts[s[left]]
            left += 1
        max_length = max(max_length, right - left + 1)
        right += 1
    return max_length


# Test Cases
# print(longest_k_distinct("eceba", 2))      # 3
# print(longest_k_distinct("aa", 1))         # 2
# print(longest_k_distinct("abcba", 2))      # 3
# print(longest_k_distinct("", 3))           # 0
# print(longest_k_distinct("abc", 0))        # 0

"""
What counts represents: A dictionary that stores character:freqeuncy pairs in order to properly shrink our variable-sized window
What makes the window valid: Everything in s[left:right + 1] is a contiguous substring that has no more than k distinct characters
The invariant: After shrinking, the contiguous substring s[left:right+1] will have at most k distinct characters.
What should happen when k <= 0: This should just return 0 since there are no possible substrings of that length.
"""


def character_replacement(s: str, k: int) -> int:
    """
    Return the length of the longest contiguous substring
    that can be turned into one repeated character using
    at most k replacements.
    'aaaaaa', 1 ->  6
    'aaaaab', 1 -> 6
    'babs', 1, 3
    """
    counts = {}
    left = 0
    right = 0
    max_length = 0
    max_freq = 0

    while right < len(s):
        counts[s[right]] = counts.get(s[right], 0) + 1
        max_freq = max(max_freq, counts[s[right]])
        while (right - left + 1) - max_freq > k:
            counts[s[left]] -= 1
            if counts[s[left]] == 0:
                del counts[s[left]]
            left += 1
        max_length = max(max_length, right - left + 1)
        right += 1
    return max_length


"""
What does the frequency dictionary represent? The freqeuncy dictionary 'counts' represents the character:frequency pairs of the current window. Which means all of the distinct characters and their frequencies
are stored in this that belong in the window.
What does max_frequency represent? max_frequency 'max_freq' represents the frequency of the most frequent character in the window.
How many replacements does the current window require? The current window will require (right - left + 1) - max_freq replacements
What makes the window invalid? A window is invalid if there are too many required replacements, (right - left + 1) - max_freq > k.
What is the invariant after shrinking? After shrinking, counts will represent the distinct characters and each of their frequencies of the characters in the window s[left:right+1] and our window
will contain a length of chracters where there are at most k characters that, when replaced, create a contiguous repeating character of size right - left + 1.
"""

# Test cases
# print(character_replacement("ABAB", 2))  # 4
# print(character_replacement("AABABBA", 1))
# print(character_replacement("AAAA", 0))
# print(character_replacement("", 2))


def contains_permutation(pattern: str, text: str) -> bool:
    """
    Return True if text contains a contiguous substring
    that is an anagram of pattern.
    """
    # assume that there are no empty patterns because if there were then we would just return true right?
    if len(text) < len(pattern):
        return False

    pattern_bucket = [0] * 26
    window_bucket = [0] * 26
    left = 0
    right = 0
    while right < len(pattern):
        p_index = ord(pattern[right]) - ord('a')
        t_index = ord(text[right]) - ord('a')
        pattern_bucket[p_index] += 1
        window_bucket[t_index] += 1
        right += 1

    if pattern_bucket == window_bucket:
        return True

    while right < len(text):
        window_bucket[ord(text[left]) - ord('a')] -= 1
        window_bucket[ord(text[right]) - ord('a')] += 1
        if window_bucket == pattern_bucket:
            return True
        left += 1
        right += 1
    return False


"""
Time complexity is: O(n) 
Space complexity is: O(1)
Why zero value keys should be deleted: I did not use dictionaries on this attempt
Why this is fixed-size rather than variable-sized: This is because in order for a suibstring to be considered an anagram of our pattern, it must be of the same size, thus we only look at sub
strings of size len(pattern) which is a fixed size. 
"""

print(contains_permutation("ab", "eidbaooo"))
print(contains_permutation("abc", "eidbaooo"))
print(contains_permutation("aib", "eidbaooo"))
print(contains_permutation("ab", "e"))


# BEFORE MOVING ON, MAKE THIS BUCKET ARRAY SOLUTION EFFICIENT WITHOUT LOOKING AT SOLUTION
