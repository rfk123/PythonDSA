

def find_closest_number(nums: list[int]) -> int:
    closest = nums[0]
    for i in range(1, len(nums)):
        if abs(nums[i]) <= abs(closest):
            closest = nums[i]
    return closest


print(find_closest_number([-4, -1, 1, 5, 8]))
