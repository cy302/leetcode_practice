# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # one pointer traverse
        # dummy = ListNode(0)
        # dummy.next = head
        # l = 0
        # first = head
        # while first is not None:
        #     l += 1
        #     first = first.next
        # l -= n
        # first = dummy
        # while l > 0:
        #     l -= 1
        #     first = first.next
        # first.next = first.next.next
        # return dummy.next

        # two pointers traverse
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        for i in range(n+1):
            first = first.next
        while first is not None:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next
