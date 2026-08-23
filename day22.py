
# 3Sum
def three_sum(nums: list[int]) -> list[list[int]]:
    """
    Return all unique triplets [a, b, c] such that:
    a + b + c == 0

    The answer must not contain duplicate triplets.
    """
    pass


# Test cases
three_sum([-1, 0, 1, 2, -1, -4])
# [[-1, -1, 2], [-1, 0, 1]]

three_sum([0, 1, 1])
# []

three_sum([0, 0, 0])
# [[0, 0, 0]]

# Answer these questions before coding but think of a solution before looking at these
"""
Why might sorting the array help? Sorting would allow us to use two converging pointers with a fixed number at index i to use the two sum pattern.
If you fix one number at index i, what familiar problem does the rest become?
Where should the other two pointers start?
If the total is too small, which pointer should move?
If the total is too large, which pointer should move?
How can duplicate triplets arise?
Where do you think duplicate skipping needs to happen?
What do you expect the time and space complexity to be?
"""
