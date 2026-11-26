
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


# print(longest_consectuive_subarray_with_sum_k([-2, -1, 2, 1], 1))


def k_most_freq(nums: list[int], target: int) -> list[int]:
    result = []
    frequencies = {}
    for i in range(len(nums)):
        frequencies[nums[i]] = frequencies.get(nums[i], 0) + 1

    bucket = [[] for _ in range(len(nums) + 1)]

    for key in frequencies:
        print(frequencies[key])
        bucket[frequencies[key]].append(key)

    for j in range(len(bucket) - 1, 0, -1):
        if len(result) >= target:
            break
        result.extend(bucket[j])

    return result[:target]


# print(k_most_freq([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2))


def k_most_freq_hm(nums: list[int], target: int) -> list[int]:
    freqs = {}
    for i in range(len(nums)):
        freqs[nums[i]] = freqs.get(nums[i], 0) + 1

    # Our freqeuncy array has been built out and now we just need to sort and slice
    return sorted(freqs.keys(), key=lambda item: freqs[item], reverse=True)[:target]


print(k_most_freq_hm([1, 2, 1, 2, 1, 2, 3,
      1, 2, 3, 2, 3, 3, 3, 3, 3, 3, 3], 2))


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def path_sum(node: TreeNode, sum: int) -> bool:
    if not node:
        return False

    if not node.left and not node.right:
        return sum == node.val

    return (
        path_sum(node.left, sum - node.val)
        or
        path_sum(node.right, sum - node.val)
    )


"""
what each recursive call is responsible for: to check if either subtree has a valid path to sum
why None returns False: None returns false because there is no node 
why we use or between the left and right recursive calls instead of and: because we just need one path
"""


# def lca(node: TreeNode, q: int, p: int) -> TreeNode | None:
#     if not node:
#         return None

#     if


def rotate_left(s: str, k: int) -> str:
    if not s:
        return ""
    split_point = len(s) - (k % len(s))
    return s[split_point:] + s[:split_point]


print(rotate_left("0123456", 8))


# [0,1,2,3,4,5,6]
#


# binary search practice
# Find if a value exists in the array

def bst(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (right + left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


print(bst([0, 1, 2, 3, 4, 7, 10, 11, 13], 3))


def expected_index(nums: list[int], target: 9):
    # Use

    pass


class Hash:
    def __init__(self, size=8):
        self.size = size
        self.cells = [[] for _ in range(size)]

    def index(self, key):
        return sum(ord(c) for c in key) % self.size

    def put(self, key, value):
        cell = self.cells[self.index(key)]
        for pair in cell:
            if pair[0] == key:
                pair[1] = value
                return
        cell.append([key, value])

    def get(self, key):
        for k, v in self.cells[self.index(key)]:
            if k == key:
                return v
        return None


# counting
# return the character with the highest freqeuncy in the array
def max_freq(word: str) -> str:
    frequencies = {}
    clean_word = "".join(word.split(' '))
    for char in clean_word:
        if not char.isalpha():
            return -1
        frequencies[char] = frequencies.get(char, 0) + 1

    max_char = None
    max_freq = 0
    print(frequencies)
    for c, f in frequencies.items():
        if f > max_freq:
            max_freq = f
            max_char = c

    return max_char


print(max_freq("astronomy rules the world"))


def max_freq_quick(frequencies: dict) -> str:
    return max(frequencies.items(), key=lambda x: x[1])[0]


print(max_freq_quick({'a': 1, 's': 2, 't': 2, 'r': 3, 'o': 3, 'n': 1,
      'm': 1, 'y': 1, 'u': 1, 'l': 2, 'e': 2, 'h': 1, 'w': 1, 'd': 1}))


def group_anagrams(words: list[str]) -> list[list[str]]:
    anagrams = {}
    for word in words:
        new_word = "".join(sorted(word))
        if not new_word in anagrams:
            anagrams[new_word] = []
        anagrams[new_word].append(word)
    return list(anagrams.values())


print(group_anagrams(['car', 'rac', 'bik', 'mac', 'cam', 'ball', 'acm']))


def reverse_span(s: str, left: int, right: int) -> str:
    if left > 0:
        return s[:left] + s[right: left - 1: -1] + s[right + 1:]
    return s[right::-1] + s[right + 1:]


# the time complexity is O(n) and space complexity is O(k) where k is the size of the biggest sliced substring from s
# I believe that the time complexity is O(n) because we go through each element in the original string at most once. The space complexity should be
# based off of the largest auxiliary added memory which would be the largest substring of size k so O(k). However, it might actually be just O(n) if you
# add all of the auxiliary memory used together. Time complexity O(n) and space complexity O(n). Final answer.


print(reverse_span("abcdefg", 2, 5))    # "abfedcg"
print(reverse_span("abc", 0, 2))      # "cba"
print(reverse_span("abc", 1, 1))      # "abc"
print(reverse_span("python", 1, 4))     # "pohtyn"
