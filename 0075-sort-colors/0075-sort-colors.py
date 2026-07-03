class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        count0 = 0
        count1 = 0
        count2 = 0
        for i in range(n):
            if nums[i]==0:
                count0 += 1
            if nums[i]==1:
                count1 += 1
            if nums[i]==2:
                count2 += 1

        inx = 0
        for i in range(count0):
            nums[inx] = 0
            inx +=1
          
        for i in range(count1):
            nums[inx] = 1
            inx +=1
            
        for i in range(count2):
            nums[inx] = 2
            inx +=1
        return nums
               