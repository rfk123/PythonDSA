

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
