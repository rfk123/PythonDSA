
# 3Sum
def three_sum(nums: list[int]) -> list[list[int]]:
    """
    Return all unique triplets [a, b, c] such that:
    a + b + c == 0

    The answer must not contain duplicate triplets.
    """
    result = []
    i = 0
    nums.sort()
    while i < len(nums) - 2:
        if i > 0 and nums[i] == nums[i-1]:
            i += 1
            continue
        left = i + 1
        right = len(nums) - 1
        while left < right:
            triplet_sum = nums[i] + nums[right] + nums[left]
            if triplet_sum > 0:
                right -= 1
            elif triplet_sum < 0:
                left += 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1

                while left < right and nums[left] != nums[left - 1]:
                    left += 1

                while left < right and nums[right] != nums[right + 1]:
                    right -= 1
        i += 1
    return result


# Test cases
print(three_sum([-1, 0, 1, 2, -1, -4]))
# [-4, -1, -1, 0, 1, 2]
# [[-1, -1, 2], [-1, 0, 1]]

print(three_sum([0, 1, 1]))
# []

print(three_sum([0, 0, 0]))
# [[0, 0, 0]]

# Answer these questions before coding but think of a solution before looking at these
"""
Why might sorting the array help? Sorting would allow us to use two converging pointers with a fixed number at index i to use the two sum pattern.
If you fix one number at index i, what familiar problem does the rest become? It is just 2sum with a fixed value 
Where should the other two pointers start? One index to the right of the fixed value and one at the end of the array
If the total is too small, which pointer should move? the pointer on the left should move inwards
If the total is too large, which pointer should move? the pointer on the right should move inwards
How can duplicate triplets arise? If we have seen the same fixed value before 
Where do you think duplicate skipping needs to happen? I would imagine that we need to not use the same fixed values to start any of our triplets
What do you expect the time and space complexity to be? I expect O(nlogn) time complexity and O(1) space
"""
