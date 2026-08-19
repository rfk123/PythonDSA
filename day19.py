

# Prefix sum plus hashmap algorithm with less scaffolding

def longest_subarray_sum_k(nums: list[int], k: int) -> int:
    """
    Return the length of the longest contiguous subarray
    whose sum equals k.
    """
    starts = {0: -1}
    max_length = 0
    current_sum = 0

    for i, num in enumerate(nums):
        current_sum += num
        difference = current_sum - k
        if difference in starts:
            max_length = max(max_length, i - starts[difference])
        if current_sum not in starts:
            starts[current_sum] = i

    return max_length


# Test Cases
longest_subarray_sum_k([1, -1, 5, -2, 3], 3)  # 4
longest_subarray_sum_k([-2, -1, 2, 1], 1)     # 2
# 1: 0, 0: 1, 5: 1, 3: 2
# Try to answer these questions before coding
"""
Why is normal sliding window unreliable? The normal sliding window approach is unreliable because we cannot move monotonicaly through this array. This is because negative integers are allowed inside of 
our input array nums. Having negative integers means that moving in a certain direction is unpredictable. For example, if all of the integers inside the input array were positive then we can tell that 
"hey, if our current subarray sum is > k then we need to shrink from the left. Or if the current subarray is < k then we need to grow to the right" We cannot do this since a subarray may be equal to k but 
then the following values could be 1 and -1 which would extend the length of the valid subarray by two but the two pointer technique would not pick up on that.
If current_sum - k appeared earlier, what does that tell you? This should tell us that there is a valid starting point somewhere in the array for a contiguous subarray up to the current index that sums to k.
For this problem, should the hashmap store a frequency or an index? I think that we are going to need the indices of starting points so I would imagine that we want to store the starting point of the possible
subarrays.
If it stores an index, do you want the earliest occurrence or the most recent occurrence? Why? You want the earliest occurence because we are only concerned with the longest contiguous subarrays.
"""
