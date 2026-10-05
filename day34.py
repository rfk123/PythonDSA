
def min_window(s: str, t: str) -> str:
    """
    Return the minimum substring of s containing all chars of t
    with the required frequencies.
    Return "" if impossible.
    """
    result = len(t) + 1

    s_dict = {}
    right = 0
    left = 0
    fit = 0
    t_dict = {}
    for char in t:
        t_dict[char] = t_dict.get(0, char) + 1

    required = len(t_dict)
    while right < len(s):
        s_dict[s[right]] = s_dict.get(0, s[right]) + 1

        if t_dict[s[right]] and s_dict[s[right]] == t_dict[s[right]]:
            fit += 1

        while fit == required:
            result = min(result, right - left + 1)
            if t_dict[s[left]]:
                fit -= 1
            s_dict[s[left]] -= 1
            if s_dict[s[left]] == 0:
                del s_dict[s[left]]

        right += 1
