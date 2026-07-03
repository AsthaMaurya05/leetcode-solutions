class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        s = 0
        min_len = float('inf')
        for i in range(len(nums)):
            s += nums[i]
            while s >= target:
                min_len = min(min_len, i - left + 1)
                s -= nums[left]
                left += 1
        return min_len if min_len != float('inf') else 0