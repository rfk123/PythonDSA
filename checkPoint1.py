
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


def product_except_self(nums: list[int]) -> list[int]:
    n = len(nums)
    result = []
    for i in range(len(nums)):
        left = i - 1
        right = i + 1
        product_without = 1
        while left >= 0 or right < len(nums):
            if left >= 0:
                product_without *= nums[left]
                left -= 1
            if right < len(nums):
                product_without *= nums[right]
                right += 1
        result.append(product_without)
    return result


print(product_except_self([0, 2, 10]))

# """ What info do I need to store? Maybe an array of prefix products?
# What pattern/structure fits? I'll need an array
# What does each pointer/variable represent?
# What makes the current state valid?
# What is the time complexity?
# What is the space complexity?
# """


def same_unique_characters(s: str, t: str) -> bool:
    """
    Return True when s and t contain the same distinct characters.
    Frequencies do not matter.
    """
    unique_s = set(s)

    for char in t:
        if char not in unique_s:
            return False

    return True


print(same_unique_characters("aab", "abcb"))
