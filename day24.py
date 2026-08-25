
# Merge sorted array
def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    nums1 has length m + n.
    The first m elements are valid sorted values.
    The last n positions are empty placeholders.

    Merge nums2 into nums1 in-place so nums1 is fully sorted.
    """
    pass


# Test Cases
nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]

merge(nums1, 3, nums2, 3)

# nums1 == [1, 2, 2, 3, 5, 6]


# Answer these questions before coding but think of a solution before reading these
"""
Why might merging from the front create a problem?
Where should the three relevant pointers start?
Should you place the smaller or larger value first?
What should happen when one array is exhausted?
What invariant should hold for the portion of nums1 that has already been filled?
What are the time and space complexities?
"""
