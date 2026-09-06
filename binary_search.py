

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
