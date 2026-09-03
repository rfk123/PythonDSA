

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
