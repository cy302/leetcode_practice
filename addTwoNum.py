# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        current = 0
        carry = 0
        rList = None
        while l1 or l2 or carry != 0:
            current += carry
            if l1:
                current += l1.val
                l1 = l1.next
            if l2:
                current += l2.val
                l2 = l2.next
            carry = current // 10
            current = current % 10

            if rList is None:
                rList = ListNode(current)
                head = rList
            else:
                rList.next = ListNode(current)
                rList = rList.next
            current = 0
        return head
