
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


print(longest_two_distinct("eceba"))   # 3, from "ece"
print(longest_two_distinct("ccaabbb"))  # 5, from "aabbb"
print(longest_two_distinct(""))        # 0
print(longest_two_distinct("aaaa"))    # 4


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
