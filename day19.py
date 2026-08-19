

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


def find_max_length(nums: list[int]) -> int:
    """
    Given a binary array containing only 0s and 1s,
    return the maximum length of a contiguous subarray
    containing an equal number of 0s and 1s.
    """
    starts = {0: -1}
    max_length = 0
    current_sum = 0

    for i, num in enumerate(nums):
        if num == 0:
            current_sum -= 1
        else:
            current_sum += 1
        if current_sum in starts:
            max_length = max(max_length, i - starts[current_sum])
        else:
            starts[current_sum] = i

    return max_length


# Test cases
print(find_max_length([0, 1]))           # 2
# {0:-1, -1: 0, }
print(find_max_length([0, 1, 0]))        # 2
print(find_max_length([0, 0, 1, 0, 1, 1]))  # 6

# Questions to answer before coding
# Try to think about the solution before reading these
"""
How could you transform the problem so that “equal number of 0s and 1s” becomes a subarray sum condition? I'm not sure if this is a dumb idea but maybe give 0s a value of negative 1. this way our subarray sum will
be balanced if the sum equals 0.
Once transformed, what prefix-sum value repeating at two different indices would tell you? If you see prefix sums of the same value then you know their is no change (aka a balance of 0s and 1s) between those two 
points and we should consider that subarrays length
Should the hashmap store frequencies or indices? Since we want to keep track of valid starting points, I think it is best to store the index
If indices, earliest or most recent? We will want to store the earlist occurence since we are only concerned with max length
What should the hashmap be initialized with? {0: -1} this is because when we find a prefix sum of 0 that means that the entire array up to this point is balanced with 0s and 1s
"""


# Next problem is continous subarray sum
def check_subarray_sum(nums: list[int], k: int) -> bool:
    """
    Return True if there exists a contiguous subarray
    of length at least 2 whose sum is a multiple of k.
    """
    return False


# Test cases
check_subarray_sum([23, 2, 4, 6, 7], 6)   # True
check_subarray_sum([23, 2, 6, 4, 7], 6)   # True
check_subarray_sum([23, 2, 6, 4, 7], 13)  # False

# Answer these before writing out the code but try to think through a solution before reading them
"""
If two prefix sums have the same remainder % k, what does that tell you about the sum between them?
Since we only need True or False, do we need remainder frequencies?
What information do we need in order to enforce subarray length at least 2?
If the same remainder appears multiple times, should we keep its earliest or latest index?
Based on what we just discussed about the imaginary empty prefix, what should the hashmap initially contain?
"""
