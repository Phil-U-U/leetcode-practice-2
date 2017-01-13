'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

Author: Phil H. Cui
Date: 01/10/27

'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int 
        :rtype: List[int]
        """
        lookup = {}

        for i, num in enumerate(nums):
        	if (target - num) not in lookup:
        		lookup[num] = i
        	else:
        		return lookup[target-num], i



if __name__ == "__main__":    
    nums, target = [2, 7, 11, 15], 9
    print Solution().twoSum( nums, target )
