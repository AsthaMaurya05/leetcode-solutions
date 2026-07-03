
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(p)>len(s):
            return []
        count = [0]*26
        for c in p:
            count[ord(c)-ord('a')]+=1
        res = []
        for i in range(len(p)):
            count[ord(s[i])-ord('a')]-=1
        if all(x==0 for x in count):
            res.append(0)
        for i in range(len(p),len(s)):
            count[ord(s[i])-ord('a')]-=1
            count[ord(s[i-len(p)])-ord('a')]+=1
            if all(x==0 for x in count):
                res.append(i-len(p)+1)
        return res
        