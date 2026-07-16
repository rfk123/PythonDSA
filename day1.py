

# Today's first exercises

def contains_duplicate(nums: list[int]) -> bool:
    # Firstly, I need to figure out which data structure is best for this problem
    # To check if a string or list contains a duplicate we would want to use a set because sets hold unique data and nothing else
    # If I scan through the input list/string and place each value into the set, I can check on each step if the set already contains that value
    # If it does then we have a duplicate else we keep moving through the end of the list/string. If I reach the end without an early exit then i return false
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


# The time complexity for contains_duplicate is O(n) since we loop through our input array once (visiting every value at most once)
# The space complexity is O(n) because the set can scale with our nums array if every value in nums is unique
print(contains_duplicate([]))  # False
print(contains_duplicate([1, 23, 3, 4, 5, 6, 23, 0]))  # True


def build_frequency_map(nums: list[int]) -> dict[int, int]:
    # The name gives it away but we want to use a dict data structure for this problem since we are storing a values count alongside of it
    # on each iteration of the input list we either add a value to our hashmap or increment an already existing key-value pair's value by 1
    # The key in our dict will act as the number and the coinsiding value will be that numbers frequency in the input array
    frequency_count = {}
    for num in nums:
        frequency_count[num] = frequency_count.get(num, 0) + 1

    return frequency_count


# The time complexity for build_frequency_map is O(n) because we scan through the input array once visiting every value at least once
# The space complexity is O(n) in worst case where every value in the input array is unique
# {1: 2, 2: 2, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1}
print(build_frequency_map([1, 2, 3, 4, 5, 6, 7, 8, 1, 2]))
print(build_frequency_map([]))  # {}


def two_sum(nums: list[int], target: int) -> list[int]:
    # To decide on a data structure for this problem I need to consider the values I need stored
    # This function will check to see if two values in the list sum to the target value so and return the indices of those values
    # This means we need to store the number and their index so a hashmap will work fine
    # On each iteration throughout the number list we will check to see if there is a number that sums with the current number to equal the target value
    # In order to do so we just take the difference between the target and the current num and search our hashmap for it (which takes o(1) lookup time)
    seen = {}
    for i, num in enumerate(nums):
        difference = target - num
        if difference in seen:
            return [seen[difference], i]
        seen[num] = i  # if num is already in seen it is fine to replace its indice in our key-value pair since we are only required to return a valid pair
    return []
# The time complexity for two_sum is O(n) since we scan through the input array visiting every value at most once (if there was no valid pair then we would scan the whole list)
# The space complexity is O(n) since if there is no pair that means seen will be the same size as our input array


print(two_sum([2, 9, 10, 1], 8))  # -1
print(two_sum([1, 2, 10, 4, 12], 16))  # [3, 4]


"""
Next Group of Questions
"""


def first_duplicate(nums: list[int]) -> int | None:
    # Return the first value that appears for a second time while scanning left to right
    # Lets try using a brute force approach at first
    # My idea of a brute force solution to this problem would be go through every possible pair in the array until we find the solution or not
    # I think an optimized solution would just be to use a hashmap to store each number and its frequency in the array
    # Once we have that hashmap we can loop through the hashmap and return the first key that has a value of > 1.
    # This optimized approach is O(n) instead of O(n^2)
    # This is banking on the hope that hashmaps store the values in the order they were inserted
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
        if count[num] > 1:
            return num
    return None


# The time complexity for this first_duplicate function is O(n) It takes O(n) to fill our dictionary and then it takes O(k) to loop through the hashmap so O(n) + O(k) is just O(n)
# The space complexity is O(n) worst case since our input array may be made of all unique values and thus our hashmap would be of the same size as the input array
print(first_duplicate([1, 2, 3, 41, 2, 3]))  # 2
print(first_duplicate([]))  # None


def most_frequent(nums: list[int]) -> int | None:
    # We want to return the number that appears most frequently so we want to store each unique number and have its count as well
    # We can just iterate through the input list to build a frequency map and then loop through that frequency map to find the most frequent value
    count = {}
    if len(nums) < 1:
        return None
    for num in nums:
        count[num] = count.get(num, 0) + 1
    max_value = 0
    max_key = nums[0]
    for key, value in count.items():
        if value > max_value:
            max_value = value
            max_key = key
    return max_key


# The time complexity of this function is O(n) because it takes o(n) to traverse through the input list and then O(k) to traverse through the hashmap O(n) + O(k) = O(n)
# The space complexity at worst is O(n) since every value in the input list could be unique and therefore the size of the hashmap would be the same as the size of the input array
print(most_frequent([1, 1, 1, 1, 1, 2, 2, 2, 2, 2,
      2, 2, 3, 3, 3, 4, 5, 5, 6, 7, 7, 7, 7, 7, 7, 7, 7]))
print(most_frequent([]))


def is_anagram(s: str, t: str) -> bool:
    # For is_anagram we need to think about how to compare two different strings in order to tell if they are made up of the exact same characters and character frequencies.
    # so we want to keep track of a character and its frequency which calls for a hashmap.
    # If we go through just one of the strings and build out a frequency map then we can traverse the other string and take away letters from the hashmap
    # If the hashmap is empty after we have traversed the entire string then we know that the two are anagrams (because we will make sure they are the same length before we begin) and can return True
    # Otherwise we return false
    if len(t) != len(s):
        return False
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    for char in t:
        if char in count:
            count[char] -= 1
            if count[char] == 0:
                del count[char]
        else:
            return False  # early exit
    return True
# The time complexity for this function is O(n) because the length of the words will have to be the same for the program to traverse them (it would really be O(n) + O(n) which is just O(n))
# The space complexity is O(n) because the word s may have only unique characters. However, at the end of the program this hashmap could be empty...


print(is_anagram('boo', 'oob'))
print(is_anagram('bob', 'blo'))


def contains_nearby_duplicate(nums: list[int], k: int) -> bool:
    # For this function we need to basically check if a substring contains a duplicate. the substring being size k
    # Or we can stay on theme with hashmaps and just check to see if we've seen a duplicate and check its location to see if its within k indices.
    # Lets do the hashmap approach so we need to travers the input list and store each value in the hashmap with its index. if we find that there is a
    # duplicate but outside of the k reach then we can feel free to update that keys value to the new index since that original one won't be able to have any duplicate neighbors.
    count = {}
    for i, num in enumerate(nums):
        if num in count:
            if (i - count[num]) <= k:
                return True
        count[num] = i
    return False


# The time complexity of contains_nearby_duplicate is O(n) because at worst case we visit each num in nums at most once
# The space complexity is O(n) because we create a hashmap and the size of the hashmap could equal the size of the input array if each num is unique
print(contains_nearby_duplicate([1, 2, 3, 1, 54, 7, 8], 3))  # True
print(contains_nearby_duplicate([1, 2, 3, 4, 1], 3))  # False
