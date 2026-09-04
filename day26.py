

def min_window(s: str, t: str) -> int | str:
    """
    Return the smallest substring of s that contains
    every character in t, including duplicate characters.

    Return "" if no valid window exists.
    """
    if len(s) < len(t) or len(t) == 0:
        return ""

    t_map = {}
    s_map = {}
    matching = 0
    left = 0
    right = 0
    min_length = len(s) + 1
    min_start = 0
    for i in range(len(t)):
        t_map[t[i]] = t_map.get(t[i], 0) + 1

    while right < len(s):
        s_map[s[right]] = s_map.get(s[right], 0) + 1
        if s[right] in t_map and t_map[s[right]] == s_map[s[right]]:
            matching += 1
        while matching == len(t_map):
            window_length = right - left + 1
            if window_length < min_length:
                min_start = left
                min_length = window_length
            s_map[s[left]] -= 1
            if s[left] in t_map and s_map[s[left]] < t_map[s[left]]:
                matching -= 1
            if s_map[s[left]] == 0:
                del s_map[s[left]]
            left += 1
        right += 1

    return "" if min_length == len(s) + 1 else s[min_start:min_start + min_length]


print(min_window("ADOBECODEBANC", "ABC"))  # "BANC"
print(min_window("a", "a"))                # "a"
print(min_window("a", "aa"))               # ""

"""

"""


def three_sum(nums: list[int]) -> list[list[int]]:
    """
    Return all unique triplets [a, b, c] such that:

    a + b + c == 0

    Do not return duplicate triplets.
    """
    result = []

    nums.sort()
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left = i + 1
        right = len(nums) - 1
        while left < right:
            triplet_sum = nums[i] + nums[left] + nums[right]
            if triplet_sum == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif triplet_sum > 0:
                right -= 1
            else:
                left += 1

    return result


# print(three_sum([-1, 0, 1, 2, -1, -4]))
# [-1,-1,0,1,2,4]
# # [[-1, -1, 2], [-1, 0, 1]]

# print(three_sum([0, 1, 1]))
# # []

# print(three_sum([0, 0, 0, 0]))
# [[0, 0, 0]]

"""
Why is duplicate i skipped with an if, not a while? Because we should just be moving to the next iteration of the for loop. Not sure why
I thought using a while loop would be good there. Especially since it was going to run forever since nothing was changing in the loop 
that would cause different outcomes for the condition check.
Why do we move both left and right after finding a triplet? Because if you only remove one value from the triplets then the only value
that can make those 2 remaining values == 0 is the one we have seen before. Thus, all three values have to change after we have found 
a triplet that == 0.
Why must left < right come first in the duplicate-skipping conditions? Because python actually reads and works from left to right so if we 
compare nums[right] with nums[left] before we ensure that they are both pointers that are in valid indexes then there will be error
"""
