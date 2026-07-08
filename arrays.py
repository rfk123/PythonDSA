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
    result = ['a'] * len(nums)
    right = len(nums) - 1
    n = len(nums) - 1
    left = 0
    while left < right:
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


def printWindows(nums, k):
    print(nums)
    left = 0
    right = 0
    for i in range(k):
        right += 1
    right -= 1
    while right < len(nums):
        print(nums[left:right + 1])
        left += 1
        right += 1
    return -1


printWindows([1, 30, 20, 1, 2, 3, 40, 14, 16], 3)


def reverseListInPlace(nums):
    # use two pointer solution for O(n) time complexity solution
    left = 0
    right = len(nums) - 1
    while (left < right):
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums


print(reverseListInPlace([1, 2, 3, 4, 5, 6, 7, 8, 9]))


def isPalindrome(str):
    left = 0
    right = len(str) - 1
    while (left < right):
        if str[left] != str[right]:
            return False
        left += 1
        right -= 1
    return True


print(isPalindrome("aabbaa"))


def removeDuplicates(nums):
    if not nums:
        return 0
    left = 0
    right = 0
    while (right < len(nums)):
        if nums[right] != nums[left]:
            left += 1
            nums[right], nums[left] = nums[left], nums[right]
        right += 1
    return nums[:left + 1]


print(removeDuplicates([1, 1, 2, 2, 3]))


def moveZeroes(nums):
    if not nums:
        return 0

    write = 0
    read = 0
    while (read < len(nums)):
        if nums[read] != 0:
            nums[read], nums[write] = nums[write], nums[read]
            write += 1
        read += 1
    return nums


print(moveZeroes([0, 1, 0, 2, 0, 0, 21, 11, 200, 0, 3]))


def buildPrefixArray(nums):
    result = [0]
    for num in nums:
        result.append(result[-1] + num)
    return result


print(buildPrefixArray([1, 2, 3, 4, 5, 6, 7, 8]))


# find maximum size subarray of size k
def max_sum_size_k(nums, k):
    window_sum = 0
    best = float("-inf")
    for right in range(len(nums)):
        window_sum += nums[right]
        if right >= k:
            window_sum -= nums[right - k]
        if right >= k - 1:
            best = max(best, window_sum)
    return best


print(max_sum_size_k([1, 2, 3, 2, 4, 1, 1], 4))


def twoSumBool(nums, target):
    seen = set()
    for num in nums:
        difference = target - num
        if difference in seen:
            return True
        seen.add(num)
    return False


print(twoSumBool([3, 4, 10, 21, 7, 12], 28))

# counts = {}
# counts["a"] = 2
# counts["b"] = counts.get("b", 0) + 1
# del counts["a"]
# print(counts)

# for key, value in counts.items():
#     print(key, value)


def validAnagram(str1, str2):
    counts = {}
    for char in str1:
        counts[char] = counts.get(char, 0) + 1

    for char in str2:
        if char not in counts:
            return False

        counts[char] -= 1

        if counts.get(char) == 0:
            del counts[char]

    return len(counts) == 0


print(validAnagram('csats', 'tacs'))


def twoSumDict(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        difference = target - num
        if difference in seen:
            return [seen[difference], i]
        seen[num] = i
    return []


print(twoSumDict([12, 8, 2, 19, 10], 11))


def containsDuplicate(nums):
    if not nums:
        return False
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


print(containsDuplicate([]))


def two_sum(nums, target):
    seen = set()
    for num in nums:
        difference = target - num
        if difference in seen:
            return True
        seen.add(num)

    return False


print(two_sum([9, 19, 29, 30, 8, 11, 18], 27))
print(two_sum([1, 2, 3], 2))


def findClosestNumber(nums) -> int:
    # find and return the closest number to 0 within an integer array containing positive and negative values
    # if there is a tie between multiple values then just take the greatest value between them
    # one pass through the array while maintaing a current closest
    closest = nums[0]
    for num in nums:
        if abs(num) < abs(closest):
            closest = num

    if closest < 0 and abs(closest) in nums:
        return abs(closest)

    return closest


print(findClosestNumber([0, -1, 10, 20, -4, -4, 5]))
"""
The time complexity of this program is O(n) because we visit each value in the list at most once
The space complexity of this program is O(1) because we do not require storing new data in memory
"""
