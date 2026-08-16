def longest_subarray_sum_k(nums: list[int], k: int) -> int:
    """
    Return the length of the longest contiguous subarray
    whose sum equals k.
    """
    starts = {}
    max_length = 0
    prefix_sum = [0] * len(nums)
    current_sum = 0
    # build prefix sum
    for i in range(len(nums)):
        current_sum += nums[i]
        prefix_sum[i] = current_sum
    for i, num in enumerate(prefix_sum):
        difference = num - k
        if difference in starts:
            max_length = max(max_length, i - starts[difference] + 1)
        if num not in starts:
            starts[num] = i
    return max_length


# Test Cases
print(longest_subarray_sum_k([1, -1, 5, -2, 3], 3))  # 4
print(longest_subarray_sum_k([-2, -1, 2, 1], 1))     # 2)

# Answer these questions before coding
"""
Why is normal sliding window unreliable? A normal sliding window is unreliable because the input array may contain negative values and is not sorted. This means that we cannot move our sliding window 
monotonically since the direction tells us nothing.
If current_sum - k appeared earlier, what does that tell you? It doesnt mean much unless its a prefix sum array right? If it is prefix sum array then it means we have found a valid starting point for our
subarray whose sum equals k
For this problem, should the hashmap store a frequency or an index? The hashmap should store an index so that we may ascertain the length of the subarray whose sum equals k.
If it stores an index, do you want the earliest occurrence or the most recent occurrence? Why? We would only want the earliest occurrence because we are only concerned with the longest subarrays.
"""
# [1,0,5,3,6]
