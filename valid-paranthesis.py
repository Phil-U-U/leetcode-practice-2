
'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

The brackets must close in the correct order, 
"()" and "()[]{}" are all valid but "(]" and "([)]" are not.


Author: Phil H. Cui
Date:   01/10/17
'''

class Solution(object):

	def isValid( self, S):

		stack = []

		lookup = { '(':')', '[':']', '{':'}' }

		for s in S:
			if s in lookup:
				stack.append(s)
			else:
				if not stack or s != lookup[stack.pop()]:
					return False
				# else:
				# 	if s != lookup[stack.pop()]:
				# 		return False


		return not stack



    # def isValid_2(self, S):
    #     """
    #     :type s: str
    #     :rtype: bool
    #     """
    #     stack = []

    #     lookup = { ')':'(', ']':'[', '}':'{' }

    #     for char in S:

    #     	if char in lookup:
    #     		if not stack or stack[-1] != lookup[char]:
    #     			return False
    #     		else:
    #     			stack.pop()
    #     	else:
    #     		stack.append( char )	

    #     return not stack

if __name__ == "__main__":
    s = "()[]{}"
    print "Expected:{}-Calculated:{}".format( "True", Solution().isValid( s )  )

    s1 = "([)]"
    print "Expected:{}-Calculated:{}".format( "False", Solution().isValid( s1 ) )

    s2 = "([])"
    print "Expected:{}-Calculated:{}".format( "True", Solution().isValid( s2 ) )

    s3 = "([]{})"
    print "Expected:{}-Calculated:{}".format( "True", Solution().isValid( s3 ) )
