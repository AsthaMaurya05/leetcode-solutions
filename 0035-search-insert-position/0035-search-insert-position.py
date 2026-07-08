class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        count = 0
        
        for i in range(len(nums)):
            if nums[i]< target:
                count+=1
        return count




