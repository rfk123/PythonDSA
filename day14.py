

"""
What repeated work would the brute-force solution do? The repeated work that the brute force solution would have to perform is recalculating the sum on every subarray. There would be no running sum.
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


"""
Why would a normal variable sliding window be unreliable here?
What information would a running prefix sum give us?
If the current prefix sum is current_sum, what earlier prefix sum would imply that the subarray between them sums to k?
Why might we need a dictionary of prefix-sum frequencies rather than just a set?
"""


def subarray_sum(nums: list[int], k: int) -> int | None:
    """
    Return the number of contiguous subarrays
    whose sum equals k.
    """
    # [2,3,1-1,2,3,41,-12]
    count = 0
    for j in range(len(nums)):
        current_sum = 0
        for i in range(j, len(nums)):
            current_sum += nums[i]
            if current_sum == k:
                count += 1

    return count


print(subarray_sum([1, 1, 1], 2))
