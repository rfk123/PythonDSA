

def longest_consecutive(nums: list[int]) -> int:
    """
    Return the length of the longest consecutive sequence.

    The sequence does not need to appear consecutively
    in the original array.

    Your solution should run in O(n) average time.
    """
    if not nums:
        return 0

    distinct = set()
    max_length = 0
    for i in range(len(nums)):
        distinct.add(nums[i])

    for i, num in enumerate(nums):
        current_length = 0
        if num - 1 in distinct:
            continue
        while num in distinct:
            current_length += 1
            num += 1
        max_length = max(max_length, current_length)

    return max_length


print(longest_consecutive([]))  # 4
# sequence: 1, 2, 3, 4

print(longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # 9


