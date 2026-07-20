
def first_unique_character(s: str) -> int:
    seen = {}
    for char in s:
        seen[char] = seen.get(char, 0) + 1
    for i, char in enumerate(s):
        if seen[char] == 1:
            return i
    return -1


print(first_unique_character('stars'))
