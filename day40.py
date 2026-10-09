
def longest_consecutive(nums: list[int]) -> int:
    distinct = set(nums)
    max_length = 0
    for num in distinct:
        if num - 1 in distinct:
            continue
        count = 0
        current = num
        while current in distinct:
            count += 1
            current += 1
        max_length = max(max_length, count)

    return max_length


print(longest_consecutive([1, 5, 0, 1, 3, 4, 2, 6, 7, 0]))
