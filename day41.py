def min_window(s: str, t: str) -> str:
    """
    Return the minimum substring of s containing all chars of t
    with the required frequencies.
    Return "" if impossible.
    """
    if not s or not t:
        return ""
    t_map = {}
    for char in t:
        t_map[char] = t_map.get(char, 0) + 1

    # The main idea for this problem is to count the number of accurate character frequencies in the window
    # We will shrink the window whill the number of correct frequencies is equal to the length of t_map
    matches = 0
    min_length = len(s) + 1
    min_substring = ""
    s_map = {}
    left = 0
    right = 0
    while right < len(s):
        s_map[s[right]] = s_map.get(s[right], 0) + 1
        if s[right] in t_map and s_map[s[right]] == t_map[s[right]]:
            matches += 1
        while matches == len(t_map):
            if min_length > right - left + 1:
                min_length = right - left + 1
                min_substring = s[left:right+1]
            if s[left] in t_map and s_map[s[left]] == t_map[s[left]]:
                matches -= 1
            s_map[s[left]] -= 1
            if s_map[s[left]] == 0:
                del s_map[s[left]]
            left += 1
        right += 1
    return min_substring if min_length != len(s) + 1 else ""


print(min_window("starburst", "stt"))
