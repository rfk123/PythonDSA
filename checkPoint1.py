
def valid_palindrome(s: str) -> bool:
    """
    ignore all non-alphanumeric characters and capitalization when determining whether or not the input string is a volid palindrome
    """
    left = 0
    right = len(s) - 1
    while left < right:
        while not s[right].isalnum():
            right -= 1
        while not s[left].isalnum():
            left += 1
        if s[left].lower() != s[right].lower():
            return False
        right -= 1
        left += 1
    return True


print(valid_palindrome("A man, a plan, a canal: Panama"))  # True
print(valid_palindrome("race a car"))                      # False
print(valid_palindrome(" "))                               # True


def majority_element(nums: list[int]) -> int:
    """
    Return the value that appears more than n // 2 times
    """
    frequencies = {}
    majority_element = nums[0]
    line = len(nums) // 2
    for num in nums:
        frequencies[num] = frequencies.get(num, 0) + 1
        if frequencies[num] > line:
            majority_element = num
    return majority_element


print(majority_element([2, 2, 1, 1, 1, 2, 2]))  # 2


def character_replacement(s: str, k: int) -> int:
    """
    you may replace k characters to factor into the longest length
    """
    window = {}
    left = 0
    right = 0
    max_freq = 0
    max_length = 0
    while right < len(s):
        window[s[right]] = window.get(s[right], 0) + 1
        max_freq = max(max_freq, window[s[right]])
        while (right - left + 1) - max_freq > k:
            window[s[left]] -= 1
            left += 1
        max_length = max(max_length, right - left + 1)
        right += 1
    return max_length


print(character_replacement("ABAB", 2))      # 4
print(character_replacement("AABABBA", 1))   # 4)
