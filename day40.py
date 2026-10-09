
def longest_consecutive(nums: list[int]) -> int:
    distinct = set(nums)
    max_length = 0
    for num in distinct:
        if num - 1 in distinct:
            continue
        count = 0
        current = num
        while current in distinct:
            count += 1
            current += 1
        max_length = max(max_length, count)

    return max_length


print(longest_consecutive([1, 5, 0, 1, 3, 4, 2, 6, 7, 0]))


def min_subarray_len(target: int, nums: list[int]) -> int:
    left = 0
    right = 0
    min_length = len(nums) + 1
    window_sum = 0
    while right < len(nums):
        window_sum += nums[right]
        while window_sum >= target:
            min_length = min(min_length, right - left + 1)
            window_sum -= nums[left]
            left += 1
        right += 1
    return min_length if min_length != len(nums) + 1 else 0


print(min_subarray_len(7, [2, 3, 1, 2, 4, 3]))
