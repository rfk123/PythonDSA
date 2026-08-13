

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

print(pivot_index([1, 7, 3, 6, 5, 6]))  # 3
# [1, 8, 11, 17, 22, 28]
print(pivot_index([1, 2, 3]))         # -1
print(pivot_index([2, 1, -1]))         # 0
