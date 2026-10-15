def min_window(s: str, t: str) -> str:
    """
    Return the minimum substring of s containing all chars of t
    with the required frequencies.
    Return "" if impossible.
    """
    if not s or not t:
        return ""
    t_map = {}
    for char in t:
        t_map[char] = t_map.get(char, 0) + 1

    # The main idea for this problem is to count the number of accurate character frequencies in the window
    # We will shrink the window whill the number of correct frequencies is equal to the length of t_map
    matches = 0
    min_length = len(s) + 1
    min_substring = ""
    s_map = {}
    left = 0
    right = 0
    while right < len(s):
        s_map[s[right]] = s_map.get(s[right], 0) + 1
        if s[right] in t_map and s_map[s[right]] == t_map[s[right]]:
            matches += 1
        while matches == len(t_map):
            if min_length > right - left + 1:
                min_length = right - left + 1
                min_substring = s[left:right+1]
            if s[left] in t_map and s_map[s[left]] == t_map[s[left]]:
                matches -= 1
            s_map[s[left]] -= 1
            if s_map[s[left]] == 0:
                del s_map[s[left]]
            left += 1
        right += 1
    return min_substring if min_length != len(s) + 1 else ""


print(min_window("starburst", "stt"))


class ListNode:
    def __init__(self, val: int, next=None):
        self.val = val
        self.next = next


def remove_nth_from_end(
    head: ListNode | None,
    n: int
) -> ListNode | None:
    """
    Remove the nth node from the end of the linked list
    and return the head.
    """
    # My initial thought of this question is to make a window the size of n + 1 by using two pointers that will traverse throughout
    # the LL. In linked lists, if you want to remove a node then it is most helpful to have a pointer on the node that is pointing to the removal
    # node instead of being directly on it which is why we want the window size to be + 1 because if you take the window through the entire
    # LL then when right pointer hits None then the left pointer will be at the node directly before the removal node and we can remove
    # from there. This will be O(n) time complexity because every node is visited at least once
    right = head
    left = head
    for _ in range(n + 1):
        if right:
            right = right.next
        else:
            return None
    while right is not None:
        right = right.next
        left = left.next

    if left.next:
        left.next = left.next.next
    else:
        left.next = None
    return head


start = None
# start = ListNode(1)
# start.next = ListNode(2)
# start.next.next = ListNode(3)
# start.next.next.next = ListNode(4)


def preview_list(head):
    if not head:
        return None
    result = ""
    curr = head
    while curr:
        result += f" {curr.val} ->"
        curr = curr.next
    result += " None"
    return result


print(preview_list(remove_nth_from_end(start, 1)))

"""
Time complexity O(n) 
Space complexity O(1)
"""


def longest_consecutive(nums: list[int]) -> int:
    """
    Return the length of the longest sequence of
    consecutive integers.

    The solution should run in O(n) average time.
    """
    # Example
    # longest_consecutive([100, 4, 200, 1, 3, 2])  # 4
    """
    So this problem seems to be one of chatgpts favorite to ask me which is why i feel so familiar with it.
    What we care about here is sequences of consecutive integers. Not adjacent integers per se. So in the example we see that 
    1,2,3,4 is a sequence of consecutive integers and its size is 4. There are actually no other sequences other than 100 and 200 in the 
    input array for this example. So the problem that I had when I first approached this problem was I couldn't figure out how to 
    go about finding the sequences. I can clearly tell that 1,2,3,4 is a sequence of consecutive integers but it was hard for me to wrap 
    my head around how to write code to find this if they weren't adjacent in an ascended ordered input array. Unfortunately, I felt that I
    was forced to seek outside resources at the time to figure this one out. Once I read the solution, I realized that I had to take a second
    to consider what it actually means to consider consecutive integers that are placed in no specific order in an array. If we loop through the array,
    we start with 100. Well what does that do for us? It could be the end of a list of consecutive integers, it could me the middle, or it could be the beginning.
    Well, what the solution from the outside source showed me is that you should really only care about the beginning of sequences. I immediately 
    felt that the mentioned solution made so much sense because every value would therefore be visited at least once and at most twice which just means
    the solution scales with n since all we will be doing is counting. So anyway, what was easy for me to understand was that we needed to use
    a set to help solve this problem. The reason being is that you dont care about duplicate values and you only care about the actual distinct 
    values in the input array. Also, sets have really fast lookup time so we can easily check to see if (num + 1) is in the set. So once I had built
    the set, it was then time to go and count the length of each consecutive sequence of integers. Essentially on each value in the array you check
    to see if value - 1 is in the set. if its not, then you have the beginning of a sequence of consecutive integers and should begin a count. If it is,
    then just continue along the array. return the max_length.
    """

    max_length = 0
    distinct = set(nums)

    for num in nums:
        count = 0
        if num - 1 not in distinct:
            count += 1
            current = num
            while current + 1 in distinct:
                count += 1
                current += 1
        else:
            continue
        max_length = max(max_length, count)

    return max_length


print(longest_consecutive([100, 4, 200, 1, 3, 2]))
