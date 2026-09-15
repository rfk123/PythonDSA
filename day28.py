
def is_valid(s: str) -> bool:
    """
    s contains only:
    '(', ')', '[', ']', '{', '}'

    Return True if every opening bracket is closed
    by the correct type in the correct order.
    """
    pass


is_valid("()[]{}")   # True
is_valid("([{}])")   # True
is_valid("(]")       # False
is_valid("([)]")     # False
