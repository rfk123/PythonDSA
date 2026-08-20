

def character_replacement(s: str, k: int) -> int:
    """
    Return the length of the longest substring that can be made
    of the same character after replacing at most k characters.
    """
    max_length = 0
    max_freq = 0
    freqeuncies = {}
    left = 0
    right = 0
    while right < len(s):
        freqeuncies[s[right]] = freqeuncies.get(s[right], 0) + 1
        max_freq = max(max_freq, freqeuncies[s[right]])
        while (right - left + 1) - max_freq > k:
            freqeuncies[s[left]] -= 1
            if freqeuncies[s[left]] == 0:
                del freqeuncies[s[left]]
            left += 1
        max_length = max(max_length, right - left + 1)
        right += 1
    return max_length


# Test cases
print(character_replacement("ABAB", 2))      # 4
print(character_replacement("AABABBA", 1))   # 4

# Answer these questions before coding but think of a solution before answering
"""
Why is this a sliding-window problem rather than a prefix-sum problem? Well, firstly we are considering characters and not integers. Also we are building out subarrays that need to please a certain condition.
What information must the hashmap store? The hashmap will store unique characters and their frequencies I believe.
For a window of length L, if the most frequent character appears max_freq times, how many replacements are needed? The amount of replacements needed will be L - max_freq
When is the window invalid? The window is invalid if the number of replacements needed exceeds k.
What should happen while the window is invalid? We will shrink from the left of our window
What does max_freq represent in the standard optimized solution? max_freq represents the frequency of the character that appeared the most in the initial subarray before shrinking.
"""
