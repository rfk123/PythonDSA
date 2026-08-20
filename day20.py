

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
# print(character_replacement("ABAB", 2))      # 4
# print(character_replacement("AABABBA", 1))   # 4

# Answer these questions before coding but think of a solution before answering
"""
Why is this a sliding-window problem rather than a prefix-sum problem? Well, firstly we are considering characters and not integers. Also we are building out subarrays that need to please a certain condition.
What information must the hashmap store? The hashmap will store unique characters and their frequencies I believe.
For a window of length L, if the most frequent character appears max_freq times, how many replacements are needed? The amount of replacements needed will be L - max_freq
When is the window invalid? The window is invalid if the number of replacements needed exceeds k.
What should happen while the window is invalid? We will shrink from the left of our window
What does max_freq represent in the standard optimized solution? max_freq represents the frequency of the character that appeared the most in the initial subarray before shrinking.
"""


# Minimum size subarray sum
def min_subarray_len(target: int, nums: list[int]) -> int:
    """
    Return the minimum length of a contiguous subarray
    whose sum is >= target.

    Return 0 if no such subarray exists.

    Assume all values in nums are positive.
    """
    min_length = len(nums) + 1
    current_sum = 0
    left = 0
    right = 0
    while right < len(nums):
        current_sum += nums[right]
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1
        right += 1

    return 0 if min_length == len(nums) + 1 else min_length


# test cases
print(min_subarray_len(7, [2, 3, 1, 2, 4, 3]))  # 2
print(min_subarray_len(4, [1, 4, 4]))           # 1
print(min_subarray_len(11, [1, 1, 1, 1, 1]))    # 0

# answer these problems before writing any code but think of an answer before looking at these questions
"""
What clues in the problem statement suggest a particular pattern? I am thinking that this problem suggests using a sliding window approach because we are looking for contiguous subarray of integers
that have to match a certain condition and whether or not it matches that condition tells us how to move the window
Why does the fact that all numbers are positive matter? If there were negative values then I think we wouldn't be able to monotonically move a window throughout the array and thus would need a different pattern like hashmap 
with prefix sum or something. 
When should you expand? We should expand when the subarray sum is < target
When should you shrink? We should shrink when the subarray sum is >= target
What invariant should be true when you update the minimum length? Everytime we update the minimum length we know that the subarray window (nums[left, right + 1]) sum is >= target.
"""
