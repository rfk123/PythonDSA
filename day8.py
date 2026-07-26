

# Practice test to test knowledge

def contains_duplicate_within_k(nums: list[int], k: int) -> bool:
    # seen = {}
    # for i, num in enumerate(nums):
    #     if num in seen:
    #         if i - seen[num] <= k:
    #             return True
    #     seen[num] = i
    # return False
    seen = {}
    left = 0
    right = 0
    while right < k:
        seen[nums[right]] = seen.get(nums[right], 0) + 1
        if seen[nums[right]] > 1:
            return True
        right += 1
    while right < len(nums):
        if nums[right] in seen:
            return True
        seen[nums[left]] -= 1
        if seen[nums[left]] == 0:
            del seen[nums[left]]
        seen[nums[right]] = seen.get(nums[right], 0) + 1
        right += 1
        left += 1
    return False


print(contains_duplicate_within_k([1, 2, 3, 1], 3))
print(contains_duplicate_within_k([1, 2, 3, 1], 2))
print(contains_duplicate_within_k([1, 0, 1, 1], 1))


def longest_subarray_at_most_k_zeroes(nums: list[int], k: int) -> int:
    zeroes_count = 0
    left = 0
    right = 0
    max_length = 0
    while right < len(nums):
        if nums[right] == 0:
            zeroes_count += 1
        while zeroes_count > k:
            if nums[left] == 0:
                zeroes_count -= 1
            left += 1
        max_length = max(max_length, right - left + 1)
        right += 1
    return max_length


print(longest_subarray_at_most_k_zeroes(
    [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))  # 6

print(longest_subarray_at_most_k_zeroes([0, 0, 1, 1, 0], 1))  # 3)


def two_sum_sorted(nums: list[int], target: int) -> list[int]:
    left = 0
    right = len(nums) - 1
    while left < right:
        sum = nums[right] + nums[left]
        if sum == target:
            return [left, right]
        elif sum > target:
            right -= 1
        else:
            left += 1
    return []


print(two_sum_sorted([2, 7, 11, 15], 9))  # [0, 1]
print(two_sum_sorted([1, 2, 3, 4, 6], 6))  # [1, 3]
print(two_sum_sorted([1, 2, 3], 10))      # []


# Day 8 continued
def longest_consecutive(nums: list[int]) -> int:
    max_length = 0
    left = 0
    right = 0
    while right < len(nums):
        if right == 0:
            right += 1
            continue
        if (nums[right - 1] + 1) != nums[right]:
            left = right
        max_length = max(right - left + 1, max_length)
        right += 1
    return max_length


print(longest_consecutive([100, 4, 200, 1, 3, 2]))  # 4
print(longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # 9
print(longest_consecutive([]))  # 0)
