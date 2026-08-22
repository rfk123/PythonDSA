

# Longest subarray after deleting one element
def longest_subarray(nums: list[int]) -> int:
    """
    Given a binary array nums, return the length of the longest
    non-empty subarray containing only 1s after deleting exactly one element.
    """
    zero_count = 0
    max_length = 0
    left = 0
    right = 0

    while right < len(nums):
        if nums[right] == 0:
            while zero_count > 0:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            zero_count += 1
        max_length = max(max_length, right - left)
        right += 1
    return max_length


# Test cases
print(longest_subarray([1, 1, 0, 1]))      # 3
print(longest_subarray([0, 1, 1, 1, 0, 1, 1, 0, 1]))  # 5
print(longest_subarray([1, 1, 1]))         # 2

# Answer these questions before coding but think of a solution before you read these questions
"""
What pattern does this suggest? This problem seems to suggest using a two pointer solution with a 'zero_count'
What condition should make the window invalid? A window is invalid if it has more than one 0
What information do you actually need to track inside the window? The number of 0s (and the left and right pointers but thats not inside of the window)
Once the window is valid, why might the answer be window_length - 1 rather than just window_length? Because this means that if there is a zero in the subarray then we don't count that 0 in the length.
Why does the all-ones case matter? I dont think it does because we still have to delete an element even if the suabarray contains only 1s.
What invariant should hold after shrinking? A shrinking has complete, the subarray window will only contain at most one 0 and any amount of 1s in the range nums[left:right + 1].
"""
