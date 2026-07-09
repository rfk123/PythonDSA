
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
    # This function will look for two values (not at the same index) that sum to the target value
    # Input -> A list of integers (does not have to be sorted and can contain positive or negative integers)
    # Output -> The indices of both values in a list [first_indice, second_indice]
    """
    My first idea is that we can solve this by doing a single pass through the nums list.
    For this to work, there needs to be a hashmap which will store a past seen value and its index.
    Iterating through the list, we will look to see if the difference of target - current num is in hashmap or not.
    If the difference is in the hashmap then return the first and second indices. If not, then place the current num into the hashmap along with its index. 
    """
    seen = {}
    for i, num in enumerate(nums):
        difference = target - num
        if difference in seen:
            return [seen.get(difference), i]
        seen[num] = i
    return -1


""" Test for two_sum """
# [], 1 -> -1
# [1,2], 3 -> [0,1]
# [-2, 5], 3 -> [0,1]
# [1,2,3,4,5,6,7], 20 -> -1


def is_anagram(s, t):
    pass


def first_unique_char(s):
    pass


def group_anagrams(strs):
    pass
