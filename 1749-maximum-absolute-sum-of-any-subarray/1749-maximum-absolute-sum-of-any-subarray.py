class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currentmax = nums[0]
        maxsum = nums[0]

        currentmin = nums[0]
        minsum = nums[0]

        for i in nums[1:]:
            currentmax = max(i,currentmax+i)
            maxsum = max(maxsum,currentmax)

            currentmin = min(i,currentmin+i)
            minsum = min(minsum,currentmin)

        return max(maxsum, abs(minsum))