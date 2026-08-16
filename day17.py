
def longest_subarray_sum_k(nums: list[int], k: int) -> int:
    """
    Return the length of the longest contiguous subarray
    whose sum equals k.
    """
    starts = {}
    max_length = 0
    for i in range(len(nums)):
        difference = nums[i] - k
        if difference in starts:
            max_length = max(max_length, i - starts[difference] + 1)
        else:
            starts[nums[i]] = i
    return max_length


"""
Why is normal sliding window unreliable? A normal sliding window is unreliable because negative values are allowed in the input array. This means that we cannot monotonically move our window throughout the array 
in a way that makes sense to the problem. 
If current_sum - k appeared earlier, what does that tell you? That tells me that we have a valid starting point and end point for a subarray whose values sum to k
For this problem, should the hashmap store a frequency or an index? A frequency wouldn't make sense here because we don't care about how many subarrays there are that sum to k, we only care about the length
of the valid subarrays. So, we need to store index
If it stores an index, do you want the earliest occurrence or the most recent occurrence? Why? We would want the earliest occurence because that would be the longest available subarray with that specific starting point. 
So this means that when we find a current - k value in the dictionary we don't update the value and instead just do the max length checks and move on. 
"""
print(longest_subarray_sum_k([1, -1, 5, -2, 3], 3))  # 4
print(longest_subarray_sum_k([-2, -1, 2, 1], 1))     # 2)
