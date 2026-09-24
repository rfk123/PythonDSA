
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
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            result = mid
            right = mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return left if nums[left] == target else -1


# print(first_occurrence([1, 2, 2, 2, 4, 5], 0))  # 1)


def subarray_sum(nums: list[int], k: int) -> int:
    """
    Return the number of contiguous subarrays
    whose sum equals k.
    """
    count = 0
    current_sum = 0
    starts = {0: 1}
    for i, num in enumerate(nums):
        current_sum += num
        difference = current_sum - k
        if difference in starts:
            count += starts[difference]
        starts[current_sum] = starts.get(current_sum, 0) + 1
    return count


# print(subarray_sum([1, 1, 1], 2))  # 2
# print(subarray_sum([1, 2, 3], 3))  # 2)
