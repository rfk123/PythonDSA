

def can_construct(ransom_note: str, magazine: str) -> bool:
    if len(magazine) < len(ransom_note):
        return False

    count = {}
    for char in ransom_note:
        count[char] = count.get(char, 0) + 1

    for char in magazine:
        if char in count:
            count[char] -= 1
            if count[char] == 0:
                del count[char]

    return len(count) == 0


print(can_construct('hello', 'tryhelloagain'))
print(can_construct('poopy', 'poopi'))
