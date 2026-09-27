class ListNode:
    def __init__(self, val: int, next=None):
        self.val = val
        self.next = next


def first_occurrence(nums: list[int], target: int) -> int:
    """
    nums is sorted.
    Return the first index containing target,
    or -1 if target does not exist.
    """
    left = 0
    right = len(nums) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            result = mid
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result


"""
time complexity: O(logn)
space complexity: O(1)
one-sentence invariant/core idea: We half the search area on each itteration and assume that if their is an occurence then that occurence
will be within the range of [left:right+1]. If nums[mid] == target we have found an occurence but it may not be the first occurence
so we move the right pointer to mid - 1 since anything earlier than mid will be in [left:mid]
"""


def min_subarray_len(target: int, nums: list[int]) -> int:
    """
    nums contains positive integers.

    Return the minimum length of a contiguous subarray
    whose sum is >= target.

    Return 0 if no such subarray exists.
    """
    left = 0
    right = 0
    min_len = len(nums) + 1
    current_sum = 0
    while right < len(nums):
        current_sum += nums[right]
        while current_sum >= target:
            min_len = min(min_len, right - left + 1)
            current_sum -= nums[left]
            left += 1
        right += 1
    return min_len if min_len != len(nums) + 1 else 0


"""
time complexity: O(n)
space complexity: O(n)
one-sentence invariant/core idea: The idea is to build a variable sized window while tracking a running sum. While the running sum (the 
sum of the current window [left:right+1]) is >= target we know that this is a valid window and compare the length of the window to 
the min_len before shrinking from the left. So, build out the window by extending right if the condiiton is not met and then continuously
compare and shrink from the left while the condition is met.
"""


def has_cycle(head: ListNode | None) -> bool:
    """
    Return True if the linked list contains a cycle.
    """
    fast = head
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False


"""
time complexity: O(n)
space complexity: O(1)
one-sentence invariant/core idea: The idea is that if a cycle exists then the pointers will eventually overlap if one is going 2x the speed
of the other. Otherwise if the faster pointer hits None then there is obviously no cycle.
"""
