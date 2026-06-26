# Create a list an loop through it
nums = [1, 2, 3, 4, 5, 6]
print("Looping through the nums in nums")
for num in nums:
    print(num)

print('----------------------------------')

print("Looping through the index in nums")
for i in range(len(nums)):
    print(i)

print('----------------------------------')

print("Looping through the nums and index in nums")
for i, num in enumerate(nums):
    print(i, num)

print('----------------------------------')

age = 30
print("Conditional printing with logical statements")
if age > 80:
    print(str(age) + "-" + "Old")
elif age < 80 and age > 35:
    print(str(age) + "-" + "Middle-aged")
else:
    print(str(age) + "-" + "Young")

print('----------------------------------')


print("Given an array of positive integers, return an array of squares")


def squareArray(nums):
    for i in range(len(nums)):
        nums[i] = nums[i]**2
    return nums


print(squareArray([1, 2, 3, 4, 5]))

seen = set('start')
print(seen)
print('f' in seen)

# Return the squares in ascending order from the original array
# The original array is sorted but can have both negative and positive integers


def squares(nums):
    """
    The largest square value will be at either end of the nums array since -4**2 is 16 and 4 is 16 on example [-4,1,0,4]
    Thus, we take the square values at both ends and insert the largest value into a new array (at it's end)
    """
    result = [0] * len(nums)
    right = len(nums) - 1
    n = len(nums) - 1
    left = 0
    while left <= right:
        squaredLeft = nums[left]**2
        squaredRight = nums[right]**2
        if squaredRight > squaredLeft:
            result[n] = squaredRight
            right -= 1
        else:
            result[n] = squaredLeft
            left += 1
        n -= 1
    return result


print(squares([-4, 0, 1, 4, 10]))
