

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


def daily_temperatures(temperatures: list[int]) -> list[int]:
    unresolved_days = []
    days_til_warmer = [0] * len(temperatures)
    for i, temp in enumerate(temperatures):
        while unresolved_days and temperatures[unresolved_days[-1]] < temp:
            prev_day = unresolved_days.pop()
            days = i - prev_day
            days_til_warmer[prev_day] = days
        unresolved_days.append(i)
    return days_til_warmer

# [75, 71, 69, 72]
# [0, 2, 1, 0]

# stack, current temp, i,

# [100, 4, 200, 1, 3, 2]
# { 100, 4, 200, 1, 3, 2 }
#


def longest_consecutive_sequence(nums: list[int]) -> int:
    max_length = 0
    distinct_values = set()
    for num in nums:
        distinct_values.add(num)
    for num in nums:
        if num - 1 not in distinct_values:
            count = 1
            temp = num
            while temp + 1 in distinct_values:
                count += 1
                temp += 1
            max_length = max(max_length, count)
    return max_length


print(longest_consecutive_sequence([1, 2, 2, 3]))


def jump(nums: list[int]) -> int:
    if len(nums) == 1:
        return 0

    furthest_point = 0
    current_end = 0
    jumps = 0
    for i in range(len(nums) - 1):
        furthest_point = max(furthest_point, i + nums[i])
        if current_end == i:
            current_end = furthest_point
            jumps += 1
    return jumps


print(jump([2, 3, 1, 1, 4]))
