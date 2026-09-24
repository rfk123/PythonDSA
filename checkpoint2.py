
def length_of_longest_substring(s: str) -> int:
    window_set = set()
    max_len = 0
    left = 0
    right = 0

    while (right < len(s)):
        while s[right] in window_set:
            window_set.discard(s[left])
            left += 1
        window_set.add(s[right])
        max_len = max(max_len, right - left + 1)
        right += 1
    return max_len


print(length_of_longest_substring("abcabcbb"))  # 3
print(length_of_longest_substring("bbbbb"))     # 1
print(length_of_longest_substring("pwwkew"))    # 3
