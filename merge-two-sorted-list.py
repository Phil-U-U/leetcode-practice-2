# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
    	return "{}->{}".format(self.val, self.next)    

class Solution(object):
  #   def mergeTwoLists(self, l1, l2):
  #       """
  #       :type l1: ListNode
  #       :type l2: ListNode
  #       :rtype: ListNode
  #       """

  #       dummy = ListNode(0)
  #       cur = dummy

  #       while l1 and l2:

  #       	if l1.val < l2.val:
  #       		cur.next = l1
  #       		l1 = l1.next
  #       	else:
  #       		cur.next = l2
  #       		l2 = l2.next
  #       	cur = cur.next	
  #       	print dummy.next	
		
		# if l1:
		# 	cur.next = l1
		# elif l2:
		# 	cur.next = l2	

		# return dummy.next

	def mergeTwoList(self, l1, l2):
		dummy = ListNode(0)
        current = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        
        if l1:
            current.next = l1
        else:
            current.next = l2
		
		return dummy.next	

if __name__ == "__main__":
	l1 = ListNode(1)
	l1.next = ListNode(3)
	l1.next.next = ListNode(5)

	l2 = ListNode(2)
	l2.next = ListNode(4)
	l2.next.next = ListNode(6)

	print Solution().mergeTwoList( l1, l2)
	# print l1
	# print l2