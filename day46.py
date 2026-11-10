
# print out the elements of an array in reverse order
ages = [10, 31, 2, 9, 18, 21]
# using a while loop set a val to be decremented
j = len(ages) - 1
while j >= 0:
    # print(ages[j])
    j -= 1

# using a for loop with range where we have -1 step
# for i in range(len(ages) - 1, -1, -1):
    # print(ages[i])

z = 24


def my_print(s):

    z += s
    print(z)


# my_print(12)
# print(z)

def longest_contiguous_subarray_with_sum_k_brute(nums: list[int], target: int) -> int:
    max_length = 0
    for i in range(len(nums)):
        current_sum = 0
        for j in range(i, len(nums)):
            current_sum += nums[j]
            if current_sum == target:
                max_length = max(max_length, j - i + 1)
    return max_length


"""
This brute force approach has a time complexity of O(n^2) because it checks every possible subarray 
and the space complexity is O(1).
"""
# print(longest_contiguous_subarray_with_sum_k_brute([-2, -1, 2, 1], 1))

"""
We can optimize this solution and try to get time complexity to O(n). However, space complexity will 
need to be O(n).

Ordinary sliding window won't work because the input array allows for negative values which means growing
our window out to the right won't tell us for sure if the window sum is growing or shrinking.

For an alternative approach, I think we can consider looping through the array one time while keeping track
of prefix sums and their indices. If we have a prefix sum and its index then we can see if the current sum - the 
target sum == prefix sum and can then calculate the window length using the stored index and current index.

The invariant is something like: The prefix hashmap contains prefix sums and their earliest index which 
have all come from the left of our pointer (processed) while the [ptr:len(nums)] integers have not yet been processed.

"""


def longest_consectuive_subarray_with_sum_k(nums: list[int], target: int) -> int:
    prefix = {0: -1}
    max_length = 0
    current_sum = 0
    for i in range(len(nums)):
        current_sum += nums[i]
        difference = current_sum - target
        if difference in prefix:
            max_length = max(max_length, i - prefix[difference])
        if current_sum not in prefix:
            prefix[current_sum] = i
    return max_length


print(longest_consectuive_subarray_with_sum_k([-2, -1, 2, 1], 1))
