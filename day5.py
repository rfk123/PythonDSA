

def is_palindrome(s: str) -> bool:
    # What I need to store: nothing
    # What makes a string a palindrome? the string is the same in reverse
    # Things to consider? palindromes could be odd lengthed strings or even.
    # Inuition tells you what? To use a converging two pointer solution in order to solve this problem in just one pass
    left = 0
    right = len(str) - 1
    while (left < right):
        if (s[left] != s[right]):
            return False
        left += 1
        right -= 1
    return True


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


def move_zeroes(nums: list[int]) -> None:
    # What do I need
    pass


def remove_duplicates(nums: list[int]) -> int:
    pass
