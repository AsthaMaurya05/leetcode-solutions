class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l = sorted(nums)
        res = False
        
        for i in range(len(l),-1,-1):
            if l[i-1] == l[i-2]:
                res = True
                break
        if len(nums) == 1:
            return False
        else:
            return res

                  

        