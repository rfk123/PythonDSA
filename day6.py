
def is_palindrome(s: str) -> bool:
    left = 0
    right = len(s)
    while (left < right):
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def remove_duplicates(nums: list[int]) -> int:
    # sorted list of integers is the input
    left = 1
    right = 1
    while (right < len(nums)):
        if nums[right] != nums[left]:
            nums[left] = nums[right]
            left += 1
        right += 1
    return left


def move_zeroes(nums: list[int]) -> None:
    left = 0
    right = 0
    while (right < len(nums)):
        if nums[right] != 0:
            nums[right], nums[left] = nums[left], nums[right]
            left += 1
        right += 1


def reverse_string(s: str) -> None:
    right = len(s)
    left = 0
    while (left < right):
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


def remove_element(nums: list[int], val: int) -> int:
    """
    Remove every occurence of val in place

    Return k, where the first k positions contain
    the values that are not equal to val
    """
    left = 0
    right = 0
    while right < len(nums):
        if (nums[right] != val):
            nums[right], nums[left] = nums[left], nums[right]
            left += 1
        right += 1
    return left


def max_sum_subarray(nums: list[int], k: int) -> int | None:
    if k > len(nums) or k <= 0:
        return None
    left = 0
    right = 0
    current_sum = 0
    while right < k:
        current_sum += nums[right]
        right += 1
    largest_sum = current_sum

    while right < len(nums):
        current_sum -= nums[left]
        current_sum += nums[right]
        largest_sum = max(largest_sum, current_sum)
        left += 1
        right += 1
    return largest_sum


print(max_sum_subarray([2, 1, 5, 1, 3, 2], 3))


def max_average_subarray(nums: list[int], k: int) -> float | None:
    if k > len(nums) or k <= 0:
        return None
    current_sum = 0
    left = 0
    right = 0
    while (right < k):
        current_sum += nums[right]
        right += 1
    max_sum = current_sum
    while (right < len(nums)):
        current_sum -= nums[left]
        current_sum += nums[right]
        max_sum = max(max_sum, current_sum)
        right += 1
        left += 1
    return max_sum / k


print(max_average_subarray([5], 1))
