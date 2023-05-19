# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ptr1 = l1
        ptr2 = l2
        result = ListNode()
        result_ptr = result

        sum = 0
        carry = 0

        while ptr1 or ptr2 is not None:
            num1 = ptr1.val if ptr1 else 0
            num2 = ptr2.val if ptr2 else 0
            ptr1 = ptr1.next if ptr1 else None
            ptr2 = ptr2.next if ptr2 else None

            sum = num1 + num2 + carry
            carry = sum / 10
            sum = sum % 10

            new_node = ListNode(sum)
            result_ptr.next = new_node
            result_ptr = result_ptr.next
            num1 = num2 = sum = 0

        if carry:
            new_node = ListNode(carry)
            result_ptr.next = new_node
            result_ptr = result_ptr.next

        return result.next


