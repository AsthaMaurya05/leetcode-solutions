class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        prefix = 0
        sum_count = {0: 1} 
        for num in nums:
            prefix += num
            if prefix - k in sum_count:
                count += sum_count[prefix - k]
            sum_count[prefix] = sum_count.get(prefix, 0) + 1
        return count    
    