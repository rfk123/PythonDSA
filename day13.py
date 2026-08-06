
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
print(longest_k_distinct("eceba", 2))      # 3
print(longest_k_distinct("aa", 1))         # 2
print(longest_k_distinct("abcba", 2))      # 3
print(longest_k_distinct("", 3))           # 0
print(longest_k_distinct("abc", 0))        # 0

"""
What counts represents: A dictionary that stores character:freqeuncy pairs in order to properly shrink our variable-sized window
What makes the window valid: Everything in s[left:right + 1] is a contiguous substring that has no more than k distinct characters
The invariant: After shrinking, the contiguous substring s[left:right+1] will have at most k distinct characters.
What should happen when k <= 0: This should just return 0 since there are no possible substrings of that length.
"""
