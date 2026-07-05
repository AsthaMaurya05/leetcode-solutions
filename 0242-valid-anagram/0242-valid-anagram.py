class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        s1 = sorted(s)

        t1 = sorted(t)

        if len(s1) != len(t1):
            return False
            
        for i in range(len(s1)):
            if s1[i] != t1[i]:
                return False
                break
        return True        


           