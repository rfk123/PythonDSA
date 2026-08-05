
"""
One sentence naming the pattern: Performing a set comparison on two strings for a match in distinct characters.
The code: see below
Time and space complexity. Time complexity is O(k) where k is length of unique_t. Space complexity is O(k) + O(m) k being unique_t length and m being unique_s length.
One manual dry run: Done while speaking outloud
"""


def same_unique_characters(s: str, t: str) -> bool:
    """
    Return True when s and t contain the same distinct characters.
    Frequencies do not matter.
    """
    unique_s = set(s)
    unique_t = set(t)

    if len(unique_s) != len(unique_t):
        return False

    for char in unique_t:
        if char not in unique_s:
            return False

    return True


print(same_unique_characters("aab", "abb"))


"""
One sentence naming the pattern: 
The code: see below
Time and space complexity. 
One manual dry run: 
"""


def is_anagram(s: str, t: str) -> bool:
    """
    Return True when both strings contain exactly
    the same character frequencies.
    """
    if len(s) != len(t):
        return False

    frequency_bucket_s = [0] * 26
    frequency_bucket_t = [0] * 26

    for char_s, char_t in zip(s, t):
        index_s = ord(char_s) - ord('a')
        index_t = ord(char_t) - ord('a')
        frequency_bucket_s[index_s] += 1
        frequency_bucket_t[index_t] += 1

    return frequency_bucket_s == frequency_bucket_t


print(is_anagram("aabcb", "cbaba"))
