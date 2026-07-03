class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq = {}
        window_sum = 0
        max_sum = 0

        for i in range(k):
            window_sum += nums[i]
            freq[nums[i]] = freq.get(nums[i], 0) + 1

        if len(freq) == k:
            max_sum = window_sum

        for i in range(k, len(nums)):

            left = nums[i - k]
            window_sum -= left
            freq[left] -= 1

            if freq[left] == 0:
                del freq[left]

            right = nums[i]
            window_sum += right
            freq[right] = freq.get(right, 0) + 1

            if len(freq) == k:
                max_sum = max(max_sum, window_sum)
        return max_sum

        