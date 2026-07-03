class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        max_l = 0
        pre = 0
        index = {0: -1} 
        for i, num in enumerate(nums):
            pre += 1 if num == 1 else -1
            if pre in index:
                max_l = max(max_l, i - index[pre])
            else:
                index[pre] = i
        return max_l
        