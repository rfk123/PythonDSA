def subarrays_div_by_k(nums: list[int], k: int) -> int:
    """
    Return the number of contiguous subarrays
    whose sum is divisible by k.
    """
    count = 0
    current_sum = 0
    remainder_frequencies = {0: 1}
    for i in range(len(nums)):
        current_sum += nums[i]
        remainder = current_sum % k
        if remainder in remainder_frequencies:
            count += remainder_frequencies[remainder]
        remainder_frequencies[remainder] = remainder_frequencies.get(
            remainder, 0) + 1

    return count


"""
What does a prefix sum tell us here? Prefix sum will just tell you the sum of the window from the 0th index to the current position. 
If two prefix sums have the same remainder when divided by k, what does that imply about the subarray between them? I'm not sure how yet, but I think it
tells you that the sum between them is divisible by k. Actually it does make sense. If you add 5 to a 4 you get 9 and both 4 and 9 have remainder 4 when
% 5. This works.
Why do we want a dictionary of remainder frequencies? This will tell us how many subarrays have a sum that is divisible by k
What should the dictionary contain before we start scanning? It may need to contain a key-value pair of 0:1 since any value with the remainder of 0 once
divided by k is obviously divisble by k and counts as its own subarray.
"""

# [4,5,0,-2,-3,1], 5
# [4,9,9,7,4,5]
# [4,4,4,2,4,0]
print(subarrays_div_by_k([4, 5, 0, -2, -3, 1], 5))  # 7
print(subarrays_div_by_k([5], 9))                    # 0
