
# 3Sum closest
def three_sum_closest(nums: list[int], target: int) -> int:
    """
    Return the sum of three integers in nums
    whose sum is closest to target.
    """
    closest_sum = nums[0] + nums[1] + nums[2]
    i = 0
    nums.sort()
    while i < len(nums) - 2:
        left = i + 1
        right = len(nums) - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            current_difference = abs(target - current_sum)
            if current_difference < abs(target - closest_sum):
                closest_sum = current_sum
            if current_sum > target:
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                return target
        i += 1
    return closest_sum


# Test cases
print(three_sum_closest([-1, 2, 1, -4], 1))   # 2
print(three_sum_closest([0, 0, 0], 1))         # 0)


# Answer these questions before you code but think of a solution before you look at these
"""
Why does sorting still help here? Sorting will help us move monotonically along the array (intentional movement with our pointers since we know what it means to move up one indice or down one indice)
If you fix nums[i], where should left and right start? left pointer will start at i + 1 and right pointer will start at len(nums) - 1
How do you decide whether a new triplet sum is “better” than the best one so far? take the absolute value of the target sum minus the triplet sum and whichever is closest to 0 wins. 
If triplet_sum < target, which pointer should move? left pointer should move inwards one index
If triplet_sum > target, which pointer should move? right pointer should move inwards one index
What can you do if triplet_sum == target? return the target sum
What do you expect the time and space complexities to be? I expect a time complexity of O(n^2) and a space complexity of O(1)
"""


# 4Sum II-style pair counting
def four_sum_count(
    nums1: list[int],
    nums2: list[int],
    nums3: list[int],
    nums4: list[int]
) -> int:
    """
    Return the number of tuples (i, j, k, l) such that:

    nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
    """
    pass


# Test cases
print(four_sum_count(
    [1, 2],
    [-2, -1],
    [-1, 2],
    [0, 2]
))  # 2


# Answer these questions before coding a solution but think of a solution before looking at these
"""
What would the brute-force time complexity be? I would imagine four for loops so O(n^4)
Can you split the four-number equation into two two-number equations? yeah I guess you could have a sum from nums1
If you compute every sum from nums1 + nums2, what information should a hashmap store?
When you later compute a sum from nums3 + nums4, what complementary value are you looking for?
Why do we need frequencies rather than just a set?
What do you expect the optimized time and space complexities to be?
"""
