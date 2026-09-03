
# Merge sorted array
def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    nums1 has length m + n.
    The first m elements are valid sorted values.
    The last n positions are empty placeholders.

    Merge nums2 into nums1 in-place so nums1 is fully sorted.
    """
    k = len(nums1) - 1
    n = n - 1
    m = m - 1
    while n >= 0 or m >= 0:
        while m < 0 and n >= 0:
            nums1[k] = nums2[n]
            k -= 1
            n -= 1
        if n < 0:
            return nums1
        if nums1[m] >= nums2[n]:
            nums1[k] = nums1[m]
            m -= 1
        else:
            nums1[k] = nums2[n]
            n -= 1
        k -= 1
    return nums1


# Test Cases
nums1 = [1, 7, 0, 0, 0]
nums2 = [0, 5, 6]

print(merge(nums1, 2, nums2, 3))

# nums1 == [1, 2, 2, 3, 5, 6]


# Answer these questions before coding but think of a solution before reading these
"""
Why might merging from the front create a problem? I think the prooblem would be overwritting values.
Where should the three relevant pointers start? One pointer will be at the end of nums1 so m + n - 1, one pointer will be at the end of nums2 so n - 1, and the other pointer will be at the end of the valid 
nums in nums1 so m - 1.
Should you place the smaller or larger value first? We will want to start with the larger values because we know that the possible largest values are at the end of nums1[:m] and nums2
What should happen when one array is exhausted? we just fill in the rest of the leftover one
What invariant should hold for the portion of nums1 that has already been filled? 
What are the time and space complexities?
"""
