
def happy_number(n: int) -> bool:
    seen = set()
    tmp = n
    while (tmp != 1):
        if tmp in seen:
            return False
        seen.add(tmp)
        tmp = helper(tmp)
    return True


def helper(n: int) -> int:
    total = 0
    while n > 0:
        # peel off digits from the back of the integer and add to total the square
        digit = n % 10
        total += digit ** 2
        n //= 10
    return total


print(happy_number(19))
print('above')


def find_difference(nums1: list[int], nums2: list[int]) -> list[list[int]]:
    return1 = []
    return2 = []
    set1 = set(nums1)
    set2 = set(nums2)
    for num1, num2 in zip(nums2, nums1):
        if num1 not in set1:
            return2.append(num1)
        if num2 not in set2:
            return1.append(num2)
    return [return1, return2]


"""
Return two lists:

values that appear in nums1 but not nums2
values that appear in nums2 but not nums1

Each result should contain unique values.
"""

print(find_difference([1, 2, 3], [2, 4, 6]))


def longest_consecutive(nums: list[int]) -> int:
    seen = set(nums)
    max_count = 0
    for num in seen:
        if num - 1 not in seen:
            count = 1
            while num + 1 in seen:
                count += 1
                num += 1
            max_count = max(max_count, count)

    return max_count


print(longest_consecutive([100, 4, 200, 1, 3, 2]))


def is_isomorphic(s: str, t: str) -> bool:
    s_to_t = {}
    t_to_s = {}
    if (len(t) != len(s)):
        return False
    for chars, chart in zip(s, t):
        if chars in s_to_t and s_to_t[chars] != chart:
            return False
        if chart in t_to_s and t_to_s[chart] != chars:
            return False
        s_to_t[chars] = chart
        t_to_s[chart] = chars
    return True


print(is_isomorphic("egg", "add"))    # True
print(is_isomorphic("foo", "bar"))    # False
