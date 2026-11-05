

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

"""
what the brute-force solution would be: The brute force solution would be to consider every subarray in the input array
what complexity that would have: O(n^2)
what property of the input might allow something better: The fact that it is all positive numbers
what state/information you think you need while traversing: A window_sum, two pointers, and a min_length
what complexity you're aiming for: O(n)
"""


# You are given an integer array nums. Return True if there are two distinct indices i and j such that:
# nums[i] == nums[j]
# abs(i - j) <= k
# Otherwise return False

def abs2Sum(nums: list[int], k: int) -> bool:
    seen = {}
    for i, num in enumerate(nums):
        if num in seen:
            difference = abs(i - seen[num])
            if seen[num] != i and difference <= k:
                return True
            seen[num] = i
    return False


print(abs2Sum([1, 2, 3, 1], 3))
"""
what the brute-force solution would be:  going through each duo combination of values in the array and checking condition
what complexity that would have: O(n^2)
what property of the input might allow something better: I don't think its a property of the array that allows for something better, rather it is the use of a hashmap
what state/information you think you need while traversing: a hashmap that contains seen 
what complexity you're aiming for: O(n)
"""

nums = [10, 8, 13, 23, 3, 6]
tums = [32, 31, 30, 29, 28, 27]

# rotate the array by 4 paces
# [13,23,3,6,10,8] -> outcome
# The secret to rotating is to use the modulo operator since n rotations restore the array back to its original orientation
# take the length of the array and perform 4 % len(nums) to get the rotated index of the current value

n = len(nums)
rotated = [0] * n
for i in range(n):
    new_index = (5 + i) % n
    rotated[new_index] = nums[i]

print(rotated)

# How can you do it in place?


def valid_abreviation(word: str, abbr: str) -> bool:
    # word: 'imagination' abbr: 'i4nat2n'
    i = 0
    j = 0

    while j < len(abbr):
        # Two cases: the char in abbr is alphabetic character or numerical
        if abbr[j].isalpha():
            if abbr[j] != word[i]:
                return False
            i += 1
            j += 1
        else:
            num = 0
            if abbr[j] == '0':
                return False
            while j < len(abbr) and abbr[j].isdigit():
                num = (num * 10) + int(abbr[j])
                j += 1
            i += num

    return i == len(word) and j == len(abbr)


print(valid_abreviation('imagination', 'i4nat3'))
