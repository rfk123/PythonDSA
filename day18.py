def longest_subarray_sum_k(nums: list[int], k: int) -> int:
    """
    Return the length of the longest contiguous subarray
    whose sum equals k.
    """
    prefix_sums = {}
    max_length = 0
    current_sum = 0
    for i, num in enumerate(nums):
        current_sum += num
        difference = num - k
        if difference in prefix_sums:
            max_length = max(max_length, i - prefix_sums[difference] + 1)
    if current_sum not in prefix_sums:
        prefix_sums[current_sum] = i

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
# [1,0,5,3,6
