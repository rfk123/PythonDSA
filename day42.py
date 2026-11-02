

def subarray_sum(nums: list[int], k: int) -> int:
    # Return the total number of contiguous subarrays with the sum of k
    """
    The brute force soltuion would be to consider every contiguous subarray in the input array by using a nested loop.
    That solution would be O(n^2) time complexity and O(1) space complexity -- Not efficient

    I don't think that a normal sliding window approach would work here because it is not guaranteed that the input array
    is sorted in any particular order. Thus, we are not able to move about the array monotonically. Quick fix to explanation:
    it doesn't work because we allow for negative values in the input array so moving to the right does not strictly mean
    that the current sum is increasing.

    I think that when we arrive at an index in the array we should have the current running sum with the current value included.
    If we take the target sum and subtract the current running sum then we just need to concern ourselves with the difference and
    whether or not we have seen that difference be represented as a prefix sum (and how many occurences). So, this means that
    the useful information we need would be prefix sums and their occurences as well as a running sum.  

    I am aiming for a more time efficient solution (O(n)) but I cant think of a solution where we dont need auxiliar data
    structures such as a hashmap. so O(n) time and O(n) space
    """

    prefix_sums = {0: 1}
    count = 0
    current_sum = 0

    for num in nums:
        current_sum += num
        difference = current_sum - k
        if difference in prefix_sums:
            count += prefix_sums[difference]
        if current_sum not in prefix_sums:
            prefix_sums[current_sum] = 0
        prefix_sums[current_sum] += 1

    return count


print(subarray_sum([1, 2, -3], 0))

"""
Dry Run:
{0:1}, 0, 0
1: {0:1, 1:1}, 0, 1
2: {0:1, 1:1, 3:1}, 1, 3
3: {0:1, 1:1, 3:1, 6:1}, 2, 6 
"""


def rotated_array(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while (left <= right):
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < nums[right]:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
    return -1

# [4,5,6,7,0,1,2]
# 0
# 4

#
#
