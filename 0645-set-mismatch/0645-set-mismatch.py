class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        s = set()
        dup = -1

        for num in nums:
            if num in s:
                dup = num
            s.add(num)

        for i in range(1, n+1):
            if i not in s:
                mis = i
                break

        return [dup, mis]        