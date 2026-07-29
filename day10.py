
def isHappy(n: int) -> bool:
    # a number is happy if you continuously add the squares of n until they sum to 1
    seen = set()
    while n != 1:
        # we can detect a cycle if we revisit any previous version of n
        if n in seen:
            return False
        seen.add(n)
        n = helper(n)
    return True


def helper(n: int) -> int:
    total = 0
    while n > 0:
        digit += n % 10
        total = digit ** 2
        n //= 10
    return total


print(isHappy(19))
