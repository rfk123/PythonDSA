

"""
What repeated work would the brute-force solution do? I imagine that the brute force solution would just be comparing every contiguous subarray in the nums array of len k.
What information from the previous window can be reused? From the previous window you would know the previous window sum and the value to get rid of.
What leaves the window, and what enters? You are scanning/sliding your window from left to right along the nums list so the value that is pointed to by left is removed
and the value pointed to by right is added
What is the invariant after each slide? After each slide we have a window of contiguous integers of the range nums[left:right+1] which is just the length of k. This window contains
a running window sum as well. 
"""


def max_sum_subarray(nums: list[int], k: int) -> int | None:
    """
    Return the maximum sum of any contiguous
    subarray of exactly length k.
    """
    left = 0
    right = 0
    current_sum = 0
    while right < k:
        current_sum += nums[right]
        right += 1
    max_sum = current_sum
    while right < len(nums):
        current_sum -= nums[left]
        current_sum += nums[right]
        max_sum = max(max_sum, current_sum)
        right += 1
        left += 1
    return max_sum
