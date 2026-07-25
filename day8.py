

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
