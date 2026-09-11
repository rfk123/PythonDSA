

# binary search works when the search space (data structure) is ordered in a way that lets one comparison eliminate an entire half of the remaining candidates.
# The invariant: If the target exists, it must be somewhere within the search interval

def binary_search(nums: list[int], val: int) -> bool:
    # perform binary search on a sorted list of integers
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (right + left) // 2
        if nums[mid] == val:
            return mid
        elif nums[mid] < val:
            left = mid + 1
        else:
            right = mid - 1

    return right + 1

# O(logn) time complexity and O(1) space


nums = [1, 3, 5, 7, 9, 11]
target = 20
print(binary_search(nums, target))


def first_occurrence(nums: list[int], val: int) -> int:
    # Use binary search to find the first occurence of val in the input array
    # If no occurence then return -1
    """
    Explain thought:
    Binary search is used on data where a condition is able to split the data in half at each step in order to find something.
    First occurence could be solved with just a simple for loop but binary search allows us a more optimized solution of O(logn) instead of O(n)
    We use pointers at opposite ends to search the value at the middle of each interval. If the middle value is lower than the input value
    then we move the left pointer to mid + 1 index. If the middle value is greater than the input value then we move the right pointer
    to mid - 1. Otherwise the mid pointer is pointing to a value that matches our input value.
    My initial idea was to perform binary search until nums[mid] == value and then move our left pointer up one step at a time until 
    nums[left] == value but that doesn't really make sense for a very large input even if the array is sorted. The more efficient solution
    would be to have a result variable where we can store the indice of the first occurence of the val and every time our mid pointer points
    to a value that is == value then it updates result to be = to that index and then it moves the right pointer to mid - 1 (we don't stop 
    the search until left > right because there could be more occurences of value in [left: mid])
    """
    left = 0
    right = len(nums) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == val:
            result = mid
            right = mid - 1
        elif nums[mid] > val:
            right = mid - 1
        else:
            left = mid + 1

    return result


# print(first_occurrence([1, 2, 2, 2, 3, 4], 2))  # 1
# print(first_occurrence([1, 2, 3, 4], 3))        # 2
# print(first_occurrence([1, 2, 3, 4], 5))        # -1


def last_occurrence(nums: list[int], target: int) -> int:
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


# print(last_occurrence([1, 2, 2, 2, 3, 4], 2))  # 3
# print(last_occurrence([1, 2, 3, 4], 3))        # 2
# print(last_occurrence([1, 2, 3, 4], 5))        # -1


def search_range(nums: list[int], target: int) -> list[int]:
    """
    Return [first_index, last_index] of target in nums.
    Return [-1, -1] if target does not exist.
    """
    first = first_occurrence(nums, target)
    last = last_occurrence(nums, target)
    return [first, last]


# print(search_range([5, 7, 7, 8, 8, 10], 8))  # [3, 4]
# print(search_range([5, 7, 7, 8, 8, 10], 6))  # [-1, -1]
# print(search_range([], 0))                   # [-1, -1]


def search_rotated(nums: list[int], target: int) -> int:
    """
    Return the index of target in a rotated sorted array.
    Return -1 if target does not exist.
    """
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[right] > nums[mid]:  # if the right side is sorted
            if nums[mid] <= target <= nums[right]:  # if the val is within the range of right side
                left = mid + 1
            else:  # if it is not within that range then we should check the other side
                right = mid - 1
        # if the left side is sorted (if one side is not sorted then the other side is sorted)
        else:
            # if the target value lies within the range of nums[left:mid+1]
            if nums[left] <= target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

    return -1


print(search_rotated([3, 1], 1))  # 2
print(search_rotated([4, 5, 6, 7, 0, 1, 2], 6))  # -1
print(search_rotated([1], 0))                    # -1


def find_min(nums: list[int]) -> int:
    """
    nums was originally sorted in ascending order,
    then rotated.

    Return the minimum value.

    Assume nums contains distinct values.
    """
    if not nums:
        return -1
    left = 0
    right = len(nums) - 1
    if nums[left] <= nums[right]:
        return nums[left]
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]


# [4, 5, 1, 2, 3]
print(find_min([4, 5, 1, 2, 3]))        # 1
print(find_min([4, 5, 6, 7, 0, 1, 2]))  # 0
print(find_min([11, 13, 15, 17]))       # 11


def find_peak_element(nums: list[int]) -> int:
    """
    Return the index of any peak element.

    A peak is an element strictly greater than its neighbors.

    You may assume:
    nums[-1] = nums[n] = -infinity
    nums[i] != nums[i + 1]

    Your solution should run in O(log n).
    """
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return right


print(find_peak_element([1, 2, 3, 1]))        # 2
print(find_peak_element([0, 8, 9]))  # 1 or 5


def min_eating_speed(piles: list[int], h: int) -> int:
    left = 1
    right = max(piles)
    while left < right:
        mid = (left + right) // 2
        hours = 0
        for pile in piles:
            hours += (pile + mid - 1) // mid

        if hours <= h:
            right = mid
        else:
            left = mid + 1

    return left
