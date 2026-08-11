

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
Why would a normal variable sliding window be unreliable here? Using a normal variable-sized sliding window would not be a viable option here because the inpiut
list is not necessarily sorted and can have negative values. This means that expanding our window could increase or decrease the window's current sum.
What information would a running prefix sum give us? Using a running prefix sum, we will be given the ability to see the sum of all of the subarrays with 
quick lookup.
If the current prefix sum is current_sum, what earlier prefix sum would imply that the subarray between them sums to k?If the current prefix sum is our current_sum
It will need to be a sum that is current_sum - k
Why might we need a dictionary of prefix-sum frequencies rather than just a set? This is important to pool the counts together quickly. So if we come accross a 
5 in our prefix sum list then we do 5 - k and look to see if our dictionary has any 5 - k value. if it does what is its frequency? Because that will be the number
of subarrays that sum to k.
"""


def subarray_sum(nums: list[int], k: int) -> int:
    """
    Return the number of contiguous subarrays
    whose sum equals k.
    """
    n = len(nums)
    current_sum = 0
    count = 0
    counts = {0: 1}
    for i in range(n):
        current_sum += nums[i]
        difference = current_sum - k
        if difference in counts or difference == 0:
            count += counts[difference]
        counts[current_sum] = counts.get(current_sum, 0) + 1
    return count


print(subarray_sum([1, 1, 1], 2))
# [1,2,3]
# {1:1}
#
#
#

print(4 % 5)
