# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        left_over = 0
        dummy = ListNode()
        current = dummy
        while l1 or l2 or left_over:
            val_1 = l1.val if l1 else 0
            val_2 = l2.val if l2 else 0

            total = val_1 + val_2 + left_over
            digit = total % 10
            left_over = total // 10

            current.next = ListNode(digit)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next