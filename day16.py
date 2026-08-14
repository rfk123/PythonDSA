

def pivot_index(nums: list[int]) -> int:
    """
    Return the first index where the sum of all values
    to the left equals the sum of all values to the right.

    Return -1 if no such index exists.
    """
    prefix_sum = [0] * len(nums)
    current_sum = 0
    for i, num in enumerate(nums):
        current_sum += num
        prefix_sum[i] = current_sum

    left_sum = 0
    for i in range(len(prefix_sum)):
        if i > 0:
            left_sum += nums[i - 1]
        if left_sum == prefix_sum[-1] - prefix_sum[i]:
            return i

    return -1


"""
What would the brute-force solution repeatedly calculate? The sum of the subarray of integers to the left and the sum of the subarray of integers to the right
Do we actually need an entire prefix-sum array, or could we maintain a running sum?I think we'll need a prefix sum array for fast lookup
If total_sum is the sum of the whole array and left_sum is everything before index i, how could you calculate right_sum without another loop? right sum would just be total sum - (left_sum + nums[i])
What should left_sum represent before processing the current index? left_sum represents the sum of the subarray of the left integers to i
What is the invariant? At each step through the prefix sum array, the left_sum represents the total sum of the subarray of integers to the left of i and the 
right sum is the total_sum - (left_sum + nums[i]) which represents the sum of the subarray of integers to the right of the ith integer.
"""

# print(pivot_index([1, 7, 3, 6, 5, 6]))  # 3
# # [1, 8, 11, 17, 22, 28]
# print(pivot_index([1, 2, 3]))         # -1
# print(pivot_index([2, 1, -1]))         # 0


def build_prefix(nums: list[int]) -> list[int]:
    prefix_array = [0] * len(nums)
    current_sum = 0
    for i in range(len(nums)):
        current_sum += nums[i]
        prefix_array[i] = current_sum
    return prefix_array


def range_sum(prefix: list[int], left: int, right: int) -> int:
    """
    Return the sum of nums[left:right + 1]
    using the previously-built prefix array.
    """
    if left == 0:
        return prefix[right]
    return prefix[right] - prefix[left - 1]


"""
What exactly should prefix[i] represent? prefix[i] represents the total sum of the subarray of integers in nums from 0 to i
How can two prefix values be subtracted to isolate left...right? If you take the right sum and subtract the left sum from it you will find the 
sum between them but not including them. you could use left - 1 prefix sum and right prefix sum prefix[right] - (prefix[left-1])
What special case exists when left == 0? You can just return the right sum
Why is building a prefix array worthwhile here, whereas it was unnecessary for pivot_index? This problem requires prefix sum lookups 
What are the preprocessing time, query time, and space complexities?
"""

nums = [2, -1, 3, 5, 4]
prefix = build_prefix(nums)

print(range_sum(prefix, 1, 3))  # 7
print(range_sum(prefix, 0, 4))  # 13
print(range_sum(prefix, 2, 2))  # 3


def product_except_self(nums: list[int]) -> list[int]:
    """
    Return an array where result[i] equals the product
    of every value in nums except nums[i].

    Do not use division.
    """
    n = len(nums)
    result = [0] * n

    left_product = 1
    for i in range(n):
        result[i] = left_product
        left_product *= nums[i]
    right_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]
    return result


# [0, 0, 0, 0, 0, 0,]
# [1,2,3,2,5,1]
# [1, 1, 2, 6, 12, 70]
# After first pass^
#
"""
For position i, what two groups of numbers contribute to its answer? The group of integers to the left of i and the group of integers to the right of i (every num except for the ith)
Could you store the product of everything to the left of each index directly in result? Vague or poorly worded question. Product of everything? Not in just one pass. The product of everything to the 
left of each index CAN be stored directly in result.
After that first pass, what single running variable could represent the product of everything to the right? We can create a variable that represents the product of everything to the right, starting at 1
What should that right-side running product equal before processing the last index? Again, this wording is strange. The last index in the array or the last index processed? It will start as 1 and then multiply
that 1 by everything to the right of the ith value
What invariant does the first pass maintain? Every value at every index represents the direct amount of the product of all values to the left
What invariant does the second pass maintain? Every value at every index represents the total product of the array except for the current index value
"""
print(product_except_self([1, 2, 3, 4]))
# [24, 12, 8, 6]

print(product_except_self([-1, 1, 0, -3, 3]))
# [0, 0, 9, 0, 0])
