

def is_isomorphic(s: str, t: str) -> bool:
    # Determine whether characters in one strin can map consistently to characters in another
    if len(s) != len(t):
        return False

    s_count = {}
    t_count = {}
    for i in range(len(t)):
        s_count[s[i]] = s_count.get(s[i], 0) + 1
        t_count[t[i]] = t_count.get(t[i], 0) + 1
        if (t_count[t[i]] != s_count[s[i]]):
            return False
    return True


def word_pattern(pattern: str, sentence: str) -> bool:
    words = sentence.split(" ")
    if len(words) != len(pattern):
        return False

    word_to_char = {}
    char_to_word = {}

    for char, word in zip(pattern, words):
        if word in word_to_char and word_to_char[word] != char:
            return False
        if char in char_to_word and char_to_word[char] != word:
            return False

    return True
