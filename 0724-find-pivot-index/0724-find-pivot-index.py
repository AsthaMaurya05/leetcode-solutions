class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t_sum = sum(nums)
        l_sum = 0

        for i in range(len(nums)):
            if l_sum == t_sum - l_sum - nums[i]:
                return i
            l_sum += nums[i]
        return -1