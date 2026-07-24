
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


print(length_of_longest_substrings("abcabcbb"))
print(length_of_longest_substrings("bbbbbb"))
print(length_of_longest_substrings("abba"))
print(length_of_longest_substrings(""))


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


print(min_subarray_len(7, [2, 3, 1, 2, 4, 3]))
