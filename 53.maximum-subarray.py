#
# @lc app=leetcode id=53 lang=python
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        sumaActual = 0
        maximo = 0
        maximoNumero = nums[0]

        for i in nums:
            maximoNumero = max(maximoNumero,i)
            sumaActual += i
            if sumaActual > maximo:
                maximo = sumaActual
            if sumaActual < 0:
                sumaActual = 0

        if maximoNumero < 0:
            return maximoNumero
        return max(maximo,maximoNumero)


        
# @lc code=end

