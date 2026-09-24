
def length_of_longest_substring(s: str) -> int:
    window_set = set()
    max_len = 0
    left = 0
    right = 0

    while (right < len(s)):
        while s[right] in window_set:
            window_set.discard(s[left])
            left += 1
        window_set.add(s[right])
        max_len = max(max_len, right - left + 1)
        right += 1
    return max_len


# print(length_of_longest_substring("abcabcbb"))  # 3
# print(length_of_longest_substring("bbbbb"))     # 1
# print(length_of_longest_substring("pwwkew"))    # 3


def first_occurrence(nums: list[int], target: int) -> int:
    """
    nums is sorted.
    Return the first index containing target,
    or -1 if target does not exist.
    """
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            right = mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return left if nums[left] == target else -1


print(first_occurrence([1, 2, 2, 2, 4, 5], 0))  # 1)
