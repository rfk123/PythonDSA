def subarrays_div_by_k(nums: list[int], k: int) -> int:
    """
    Return the number of contiguous subarrays
    whose sum is divisible by k.
    """
    pass


"""
What does a prefix sum tell us here? Prefix sum will just tell you the sum of the window from the 0th index to the current position. 
If two prefix sums have the same remainder when divided by k, what does that imply about the subarray between them? I'm not sure how yet, but I think it
tells you that the sum between them is divisible by k.
Why do we want a dictionary of remainder frequencies? This will tell us how many subarrays have a sum that is divisible by k
What should the dictionary contain before we start scanning? It may need to contain a key-value pair of 0:1 since any value with the remainder of 0 once
divided by k is obviously divisble by k and counts as its own subarray.
"""

# [4,5,0,-2,-3,1], 5
# [4,9,9,7,4,5]
# [4,4,4,2,4,0]
