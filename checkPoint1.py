
def valid_palindrome(s: str) -> bool:
    """
    ignore all non-alphanumeric characters and capitalization when determining whether or not the input string is a volid palindrome
    """
    left = 0
    right = len(s) - 1
    while left < right:
        while not s[right].isalnum():
            right -= 1
        while not s[left].isalnum():
            left += 1
        if s[left].lower() != s[right].lower():
            return False
        right -= 1
        left += 1
    return True


print(valid_palindrome("A man, a plan, a canal: Panama"))  # True
print(valid_palindrome("race a car"))                      # False
print(valid_palindrome(" "))                               # True
