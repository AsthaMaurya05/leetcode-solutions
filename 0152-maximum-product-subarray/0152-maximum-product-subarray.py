class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxprod = nums[0]
        minprod = nums[0]

        ans = nums[0]

        for i in nums[1:]:
            tempmax = max(i, i*maxprod, i*minprod)
            tempmin = min(i, i*maxprod, i*minprod)

            maxprod = tempmax
            minprod = tempmin

            ans = max(ans,maxprod)

        return ans
