class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """

        l = len(gain)
        box = [0]
        for i in range(l):
            box.append(box[-1]+gain[i])
        
        return max(box)
        