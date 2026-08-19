
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
One sentence naming the pattern: Using requency bucket arrays, compare two strings to determine if they have matching unique characters and that those characters have matching frequencies.
The code: see below
Time and space complexity. Time complexity is going to be O(n) n being the length of string s/t (doesnt matter which) except for if the lengths differ. Then the time complexity is O(1). 
The space complexity will be O(1) since the bucket lists do not scale with the size of the input strings and remain size 26.
One manual dry run: Done while speaking outloud.
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

"""
One sentence naming the pattern: Using two dictionaries, determine if the two input strings have the same amount of unique characters and that those characters have one-to-one mapping relaitonships.
The code: see below
Time and space complexity. The time complexity is going to be O(n) and the space complexity may be considered linear since the max that the dictionary lengths can go to is 26 (if chars are all lower case)
One manual dry run: Done while speaking out loud
"""


def is_isomorphic(s: str, t: str) -> bool:
    """
    Return True when characters map consistently
    and one-to-one between the strings.
    """
    if len(s) != len(t):
        return False

    counts_s = {}  # 'a':'p', 'p':'b'...
    counts_t = {}  # same thing

    for char_s, char_t in zip(s, t):
        if char_s in counts_s and counts_s[char_s] != char_t:
            return False
        if char_t in counts_t and counts_t[char_t] != char_s:
            return False
        counts_s[char_s] = char_t
        counts_t[char_t] = char_s

    return True


print(is_isomorphic("egg", "add"))


"""
One sentence naming the pattern: Determine if the string s exists in string t where the characters do not need to be adjacent to one another but have to keep their relative order.
The code: see below
Time and space complexity. The time complexity is O(n) where n is the length of t. The space complexity is O(1).
One manual dry run: Done in my head
"""


def is_subsequence(s: str, t: str) -> bool:
    """
    Return True when all characters of s appear
    in t in the same relative order.

    Characters do not need to be adjacent.
    """
    if len(s) > len(t):
        return False

    ptr_s = 0
    ptr_t = 0

    while ptr_s < len(s) and ptr_t < len(t):
        if s[ptr_s] == t[ptr_t]:
            ptr_s += 1
        ptr_t += 1

    return ptr_s == len(s)


print(is_subsequence("axc", "ahbgdc"))



"""
Variable Sliding Window
| `right` | Incoming character | `left` before | Characters removed | Window after adding   | `max_length` |
| ------: | ------------------ | ------------: | ------------------ | --------------------- | -----------: |
|       0 | `"a"`              |             0 | —                  | `{"a"}` / `"a"`       |            1 |
|       1 | `"b"`              |             0 | —                  | `{"a", "b"}` / `"ab"` |            2 |
|       2 | `"b"`              |             0 | 2                  | `{"b"} / "b"`         |            2 |
|       3 | `"a"`              |             2 | -                  | `{"b", "a"} / "ba"`   |            2 |

"""


"""
| `right` | Incoming | `left` before shrinking | Counts after adding | Shrinking actions | Valid window | Maximum |
| ------: | -------- | ----------------------: | ------------------- | ----------------- | ------------ | ------: |
|       0 | `"e"`    |                       0 | `{"e": 1}`          | —                 | `"e"`        |       1 |
|       1 | `"c"`    |                       0 | `{"e": 1, "c": 1}`  | —                 | `"ec"`       |       2 |
|       2 | `"e"`    |                       0 | `{"e": 2, "c": 1}`  | —                 | "ece"        |       3 |
|       3 | `"b"`    |                       0 | `{"e": 2, "c": 1, "b": 1}`| 2 -> "ec"   | "eb"         |       3 |
|       4 | `"a"`    |                       2 | `{"e": 1, "b": 1, "a": 1}`| 1 -> "e"    | "ba"         |       3 |
"""

"""
Why does the first problem use a set? We are only concerned about duplicates in our window so if our current window already has a value that we are trying to add then we can just check that by existence
rather than a frequency count. Essentially, we just need the value and no other information about it.
Why does the second require a dictionary? We require a dictionary for this problem because we need to keep track of the length of a substring that has only two unique chars. If we were to use a set,
we wouldn't be able to find the length of something like "ecece" which is 5. Dictionaries allow us to shrink the value of a character key so that we only remove a char from our window dict if that value
reaches 0.
Why must zero-frequency keys be deleted in the second problem? This is to keep track of the characters that remain in our window. If a characters frequency count hits 0 then that means our window no longer
contains that character.
Why do both algorithms use while rather than if when shrinking? because we dont know how many times we will have to shrink so we use a while loop to continuously shrink the window while checking for 
a condition.
"""