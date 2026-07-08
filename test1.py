
def contains_duplicate(nums) -> bool:
    # This function will check to see if an integer list contains duplicates
    # Input -> a list of integers (positives and negatives)
    # Output -> boolean (true or false)
    """
    First idea is that we can solve this in just one pass through of the nums array.
    We create a set that stores unique integers found in nums.
    Every iteration of nums we check to see if the integer is in the set. If it is then we have found our duplicate. If not, then we just store the current num in the set and move to the next.
    If we get to the end of nums without finding a duplicate we can just return false.
    """
    if not nums:
        return False
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


""" Test for contains_duplicate """
# [] -> False
# [1,2,3,4,-1,-2,-3,-4,0] -> False
# [1,2,3,4,-1,2] -> True
# [-2,3,4,-1,-2,10] -> True


def two_sum(nums, target):
    pass


def is_anagram(s, t):
    pass


def first_unique_char(s):
    pass


def group_anagrams(strs):
    pass
