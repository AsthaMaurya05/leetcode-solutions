class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        left=0
        count=0
        prod = 1

        for i in range(len(nums)):
            prod *= nums[i]
            while(prod>=k):
                prod /= nums[left]
                left+=1

            count += (i-left+1)

        return count

        
            
        