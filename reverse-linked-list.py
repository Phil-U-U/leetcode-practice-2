'''
206. Reverse Linked List: Reverse a singly linked list.

Author: Phil H. Cui
Date: 01/11/2017

'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__( self ):
        return "{}->{}".format( self.val, self.next )

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(float("-inf"))

        while head:
        	dummy.next, head.next, head = head, dummy.next, head.next

        return dummy.next


if __name__ == "__main__":
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(3)

    print Solution().reverseList(l)
