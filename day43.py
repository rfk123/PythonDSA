

def min_consecutive(nums: list[int], target: int) -> int:
    # Return the minimum length of a contiguous subarray whose sum is greater than or equal to target.
    window_sum = 0
    min_length = len(nums) + 1
    left = 0
    right = 0
    while right < len(nums):
        window_sum += nums[right]
        while window_sum >= target and left <= right:
            min_length = min(min_length, (right - left) + 1)
            window_sum -= nums[left]
            left += 1
        right += 1

    return min_length if min_length != len(nums) + 1 else 0


print(min_consecutive([2, 3, 1, 2, 4, 3], 7))
