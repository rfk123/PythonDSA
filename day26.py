

def min_window(s: str, t: str) -> int | str:
    """
    Return the smallest substring of s that contains
    every character in t, including duplicate characters.

    Return "" if no valid window exists.
    """
    if len(s) < len(t) or len(t) == 0:
        return ""

    t_map = {}
    s_map = {}
    matching = 0
    left = 0
    right = 0
    min_length = len(s) + 1

    for i in range(len(t)):
        t_map[t[i]] = t_map.get(t[i], 0) + 1

    while right < len(s):
        s_map[s[right]] = s_map.get(s[right], 0) + 1
        if s[right] in t_map and t_map[s[right]] == s_map[s[right]]:
            matching += 1
        while matching == len(t_map):
            min_length = min(min_length, right - left + 1)
            s_map[s[left]] -= 1
            if s[left] in t_map and s_map[s[left]] < t_map[s[left]]:
                matching -= 1
            if s_map[s[left]] == 0:
                del s_map[s[left]]
            left += 1
        right += 1

    return min_length


print(min_window("ADOBECODEBANC", "ABC"))  # "BANC"
print(min_window("a", "a"))                # "a"
print(min_window("a", "aa"))               # ""

"""

"""
