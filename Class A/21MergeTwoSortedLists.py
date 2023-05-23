# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ptr1 = list1
        ptr2 = list2
        ptr_new = ListNode()
        new_list = ptr_new
        while ptr1 and ptr2:
            if ptr1.val <= ptr2.val:
                ptr_new.next = ptr1
                ptr1 = ptr1.next
            else:
                ptr_new.next = ptr2
                ptr2 = ptr2.next
            ptr_new = ptr_new.next
        if ptr1:
            ptr_new.next = ptr1
        if ptr2:
            ptr_new.next = ptr2

        return new_list.next


sol = Solution()
n1 = ListNode(-9)
n1.next = ListNode(3)
# n1.next.next = ListNode(4)

n2 = ListNode(5)
n2.next = ListNode(7)
# n2.next.next = ListNode(4)

merged = sol.mergeTwoLists(n1, n2)
ptr = merged
while ptr:
    print(ptr.val)
    ptr = ptr.next