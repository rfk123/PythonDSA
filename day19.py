

# Prefix sum plus hashmap algorithm with less scaffolding

def longest_subarray_sum_k(nums: list[int], k: int) -> int:
    """
    Return the length of the longest contiguous subarray
    whose sum equals k.
    """
    pass


# Test Cases
longest_subarray_sum_k([1, -1, 5, -2, 3], 3)  # 4
longest_subarray_sum_k([-2, -1, 2, 1], 1)     # 2

# Try to answer these questions before coding
"""
Why is normal sliding window unreliable?
If current_sum - k appeared earlier, what does that tell you?
For this problem, should the hashmap store a frequency or an index?
If it stores an index, do you want the earliest occurrence or the most recent occurrence? Why?
"""
