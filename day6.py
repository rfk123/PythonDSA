
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
