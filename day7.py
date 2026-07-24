
# Time to move forward in my sliding window pattern practice
# Time to practice variable-sized sliding window pattern
# Variable-sized window is just a window that's size shrinks and grows depending on some condition

# Lets first start out with the problem: longest substring without repeating characters
def length_of_longest_substrings(s: str) -> int:
    # What do I need to store? I need to keep track of what value I have seen so far in my set (the values that the window contain). All of these should be unique
    # Whats something to consider? Since we dont need to store any information other than what values coinside in the window, we can use a set.
    # If the read pointer goes out into the string and finds a character that already exists in the window then we shrink the window from the left until that is no longer the case
    # At every valid window we compare the current window's length with the max length
    if len(s) <= 0:
        return 0
    window_chars = set()
    left = 0
    right = 0
    max_length = 0
    while right < len(s):
        while s[right] in window_chars:
            window_chars.discard(s[left])
            left += 1
        window_chars.add(s[right])
        max_length = max(max_length, right - left + 1)
        right += 1
    return max_length


# print(length_of_longest_substrings("abcabcbb"))
# print(length_of_longest_substrings("bbbbbb"))
# print(length_of_longest_substrings("abba"))
# print(length_of_longest_substrings(""))


def min_subarray_len(target: int, nums: list[int]) -> int:

    current_sum = 0
    min_length = float("inf")
    left = 0
    right = 0
    while (right < len(nums)):
        current_sum += nums[right]
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1
        right += 1
    return 0 if min_length == float("inf") else min_length


# print(min_subarray_len(7, [2, 3, 1, 2, 4, 3]))


# Test of knowledge
def max_vowels(s: str, k: int) -> int:
    """
    What information must be stored? Nothing except we could create a set that contains only vowels. Other than that we will have a count and two pointers
    Which datastructure or pointer pattern fit? we will use a sliding window approach with a fixed-sized set
    Is the window fixed or variable? The window in this sliding window approach will be fixed of size k
    What makes the current state valid/invalid? the window must be of size k
    Time and space complexity? O(n) time complexity and O(1) space complexity size the size of the set is fixed ("a", "e", "i", "o", "u")
    """
    if k > len(s) or k <= 0:
        return 0
    vowels = set(["a", "e", "i", "o", "u"])
    vowel_count = 0
    left = 0
    right = 0
    while right < k:
        if s[right] in vowels:
            vowel_count += 1
        right += 1
    max_vowels = vowel_count
    while right < len(s):
        if s[left] in vowels:
            vowel_count -= 1
        left += 1
        if s[right] in vowels:
            vowel_count += 1
        right += 1
        max_vowels = max(vowel_count, max_vowels)
    return max_vowels


# print(max_vowels("abciiidef", 3))
# print(max_vowels("aeiou", 2))
# print(max_vowels("leetcode", 3))


def longest_ones(nums: list[int]) -> int:
    """
    Return the length of the longest contiguous subarray containing at most one zero
    What information must be stored? Nothing except for a zero counter, two pointers, and a max_length variable
    Which datastructure or pointer pattern fit? We just need two pointers for this 
    Is the window fixed or variable? variable
    What makes the current state valid/invalid? if there is one or fewer zeores in the subarray then that subarray is valid. else invalid
    Time and space complexity? Time complexity is O(n) and space complexity is O(1)
    """
    max_length = 0
    left = 0
    right = 0
    zeroes_count = 0
    while right < len(nums):
        if nums[right] == 0:
            zeroes_count += 1
            while zeroes_count > 1:
                if nums[left] == 0:
                    zeroes_count -= 1
                left += 1
        max_length = max(max_length, right - left + 1)
        right += 1
    return max_length


# print(longest_ones([1, 1, 0, 1, 1, 1]))
# print(longest_ones([1, 0, 1, 0, 1, 1]))
# print(longest_ones([0, 0, 0]))
