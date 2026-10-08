

# sum to numbers that are represented as strings without converting the entire string to integer

def sum_strings(num1: str, num2: str) -> str:
    if not num1 or not num2:
        return ""

    num2_ptr = len(num2) - 1
    num1_ptr = len(num1) - 1

    carry = 0
    result = []
    while num2_ptr >= 0 or num1_ptr >= 0:
        current_sum = 0
        if num2_ptr >= 0:
            current_sum += int(num2[num2_ptr])
        if num1_ptr >= 0:
            current_sum += int(num1[num1_ptr])
        current_sum += carry
        carry = current_sum // 10
        digit = current_sum % 10
        result.append(str(digit))
        num2_ptr -= 1
        num1_ptr -= 1

    if carry:
        result.append(str(carry))
    result.reverse()
    return "".join(result)


print(sum_strings("1", "9"))
print("hello")


class ListNode:
    def __init__(self, val: int, next=None):
        self.val = val
        self.next = next


def reverse_list(head: ListNode | None) -> ListNode | None:
    if not head:
        return None

    prev = None
    current = head
    while current:
        tmp = current.next
        current.next = prev
        prev = current
        current = tmp
    prev
    return prev


def output_list(head: ListNode | None) -> str | None:
    if not head:
        return None
    current = head
    result = ""
    while current:
        result += str(current.val)
        current = current.next
    return result


start = ListNode(10)
start.next = ListNode(9)
start.next.next = ListNode(8)
start.next.next.next = ListNode(7)
start.next.next.next.next = ListNode(6)
start.next.next.next.next.next = ListNode(5)

print(output_list(start))
start = reverse_list(start)
print(output_list(start))
