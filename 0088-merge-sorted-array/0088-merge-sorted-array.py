class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m,len(nums1)):
            nums1[i] = nums2[i-m]
        
        for i in range(len(nums1)):
            for j in range(i+1,len(nums1)):
                if nums1[i]>nums1[j]:
                     nums1[i], nums1[j] = nums1[j], nums1[i] 
        
        