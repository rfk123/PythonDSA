
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
