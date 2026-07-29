
def isHappy(n: int) -> bool:
    # a number is happy if you continuously add the squares of n until they sum to 1


def helper(n: int) -> int:
    total = 0
    while n > 0:
        digit = n % 10
        total = digit ** 2
        n //= 10
    return total
