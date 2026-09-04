

def sort_colors(nums: list[int]) -> list[int]:
    """
        You are given an input array of integers [0,1,2] in no specific order.
        Sort the array in-place withouth using pythons built-in sort.
    """
    low = 0
    high = len(nums) - 1
    mid = 0

    while mid <= high:
        if nums[mid] == 0:
            [nums[mid], nums[low]] = [nums[low], nums[mid]]
            mid += 1
            low += 1
        elif nums[mid] == 2:
            [nums[mid], nums[high]] = [nums[high], nums[mid]]
            high -= 1
        else:
            mid += 1

    return nums


print(sort_colors([2, 1, 0]))


def longest_subarray_sum_k(nums: list[int], k: int) -> int:
    """
    Return the length of the longest contiguous subarray
    whose sum equals k.
    """

    max_length = 0
    starting_points = {0: -1}
    current_sum = 0

    for i, num in enumerate(nums):
        current_sum += num
        difference = current_sum - k
        if difference in starting_points:
            max_length = max(max_length, i - starting_points[difference])
        if current_sum not in starting_points:
            starting_points[current_sum] = i
    return max_length


print(longest_subarray_sum_k([1, -1, 5, -2, 3], 3))
# [1,0,5,3,6]

"""
Pattern: The pattern is a single traversal with a hashmap that keeps track of prefix sums and their indexes
Hashmap represents: key-value pairs where the keys represent prefix sums and the values represent starting indices
Why {0: -1}: Because if we come accross an index in the array where the current_sum up to that point is equal to k then we know that every value from [0:i+1] sums to k 
and when we return the length of that subarray we don't count the prefix sum at the starting idice which is -1
Invariant: The invariant is something like: For every itteration through nums, nums[0:i+1] have been processed where the current_sum reflects the current running sum and
prefix sums have been stored in starting_points with the earliest index attached as their values. 
"""
