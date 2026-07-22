

def is_palindrome(s: str) -> bool:
    # What I need to store: nothing
    # What makes a string a palindrome? the string is the same in reverse
    # Things to consider? palindromes could be odd lengthed strings or even.
    # Inuition tells you what? To use a converging two pointer solution in order to solve this problem in just one pass
    left = 0
    right = len(s) - 1
    while (left < right):
        if (s[left] != s[right]):
            return False
        left += 1
        right -= 1
    return True
    # Time complexity is O(n) and space complexity is O(1)


def reverse_string(chars: list[str]) -> None:
    # What do I need to store: nothing
    # Do we have to reverse the string in place? Yes
    # Things to consider? strings of length 1 or fewer need no reversal. Also, we are given a list of chars and not a string
    # Intuition tells you what? That I can just swap characters at each end using a converging two pointer solution
    left = 0
    right = len(chars) - 1
    while (left < right):
        [chars[left], chars[right]] = [chars[right], chars[left]]
        left += 1
        right -= 1
    # Time complexity is O(n) and space complexity is O(1)


def move_zeroes(nums: list[int]) -> None:
    # What do I need to store? Nothing
    # Do we need to move or remove the zeroes? we just need to move all zeroes to the end of the list
    # Things to consider? We have to not only move the zeroes to the back of the list but also move the valid ints towards the front so there are consecutive non-zeroes starting from the beginning.
    # What does your intuition tell you? That I should use a two pointer solution where each ptr starts at the beginning of the list. One ptr goes looking for non-zeroes and the other ptr holds the spot of the first zero.
    read = 0
    write = 0
    while (read < len(nums)):
        if (nums[read] != 0):
            [nums[write], nums[read]] = [nums[read], nums[write]]
            write += 1
        read += 1
    # Time complexity is O(n) and space complexity is O(1)


def remove_duplicates(nums: list[int]) -> int:
    # What do I need to store? Nothing
    # Do I need to actually remove the duplicates from the list or do I just move them to the back of the array and return the length of the valid numbers? Return k for length of valid sublist.
    # Things to consider? I need to return the length of unique integers in the inputed list and not a new list. is this list sorted? Yes.
    # What does your intuition tell you? To use the same pattern as the move zeroes function (use a read and write ptr starting from beginning of list). That the index of the write ptr will be our k
    if not nums:
        return 0
    read = 1
    write = 1
    while (read < len(nums)):
        if nums[read] != nums[write - 1]:
            nums[write] = nums[read]
            write += 1
        read += 1
    return write
    # Time complexity is O(n) and space complexity is O(1)
