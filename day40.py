
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


def find_min(nums: list[int]) -> int:
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2

        if nums[mid] < nums[right]:
            right = mid
        else:
            left = mid + 1

    return nums[left]


print(find_min([11, 13, 15, 17]))
print(find_min([4, 5, 6, 7, 0, 1, 2]))
print(find_min([3, 4, 5, 1, 2]))


def daily_temperatures(temperatures: list[int]) -> list[int]:
    stack = []
    answer = [0] * len(temperatures)
    for i, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            start_index = stack.pop()
            answer[start_index] = (i - start_index)
        stack.append(i)
    return answer


print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))
