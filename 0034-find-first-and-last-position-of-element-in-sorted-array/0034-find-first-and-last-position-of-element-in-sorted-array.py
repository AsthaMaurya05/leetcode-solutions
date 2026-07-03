class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l,r = 0, len(nums)-1
        while l<=r :
            mid = (l+r)//2
            if nums[mid] == target:
                i,j = mid,mid
                while i>=0 and nums[i] == target:
                    i-=1
                while j<len(nums) and nums[j] == target:
                    j+=1
                return [i+1,j-1]
            if nums[mid]<target:
                l = mid+1
            else:
                r = mid-1    
        return [-1,-1]