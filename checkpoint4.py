
def subarray_sum(nums: list[int], k: int) -> int:
    """
    Return the number of contiguous subarrays whose sum equals k.
    """
    starts = {0: 1}
    count = 0
    current_sum = 0

    for num in nums:
        current_sum += num
        difference = current_sum - k
        if difference in starts:
            count += starts[difference]
        starts[current_sum] = starts.get(current_sum, 0) + 1
    return count


print(subarray_sum([10, 12, -4, 8, -10, 2, 32, -2], 26))

"""
time complexity: O(n)
space complexity: O(n)
one sentence describing the invariant or core idea: The core idea is that starts holds a record of prefix sums and their frequencies. 
These values can be seen as our 'starting points' for subarrays that may have sum == k up to the current index's position. We loop
through the input list and we check if we have seen current_sum - k in earlier sums and we'll increment the frequency of those
earlier prefix sums to our count.
"""


def last_occurrence(nums: list[int], target: int) -> int:
    """
    nums is sorted.
    Return the last index containing target,
    or -1 if target does not exist.
    """
    left = 0
    right = len(nums) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            result = mid
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return result


print(last_occurrence([0, 0, 1, 1, 1, 2, 3, 3, 4, 7, 10, 10, 11], 10))

"""
time complexity: O(logn)
space complexity: O(1)
one sentence describing the invariant or core idea: The core idea is that we are able to half our search area on every iteration because
the input list is in a particular order. If there is a solution then it will always be within the range [left:right+1].
"""


def next_greater(nums: list[int]) -> list[int]:
    """
    For each element, return the next greater value to its right.
    If none exists, use -1.
    """
    stack = []
    result = [-1] * len(nums)
    for i, num in enumerate(nums):
        while stack and nums[stack[-1]] < num:
            index = stack.pop()
            result[index] = num
        stack.append(i)
    return result


print(next_greater([10, 8, 9, 11, 2, 3, 4, 20]))

"""
time complexity:
space complexity:
one sentence describing the invariant or core idea:
"""
