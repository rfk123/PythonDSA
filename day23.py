
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
