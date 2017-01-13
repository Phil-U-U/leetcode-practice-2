'''
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

[[1,2,3],
 [4,5,6]
]

[   [4,1],
    [5,2],
    [6,3]
]

Author: Phil H. Cui
Date: 01/12/17

'''
class Solution(object):
    def rotate(self, matrix):

        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # ncols = len(matrix[0])

        for i in xrange(n-1):
        	for j in xrange(n-1-i):
        		matrix[i][j], matrix[n-1-j][n-1-i] = matrix[n-1-j][n-1-i], matrix[i][j]
		# print matrix        		

        for i in xrange(n/2):
        	matrix[i], matrix[n-1-i] = matrix[n-1-i], matrix[i] 		


if __name__ == "__main__":
    matrix = [[1,2,3], [4,5,6],[7,8,9]]
    print matrix
    Solution().rotate( matrix )
    print matrix

