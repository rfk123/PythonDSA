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
time complexity:
space complexity:
one-sentence invariant/core idea:
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
time complexity:
space complexity:
one-sentence invariant/core idea:
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
time complexity:
space complexity:
one-sentence invariant/core idea:
"""
