class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s1 = ""

        for i in s:
            if i.isalnum():
                s1 += i.lower()

        s2 = s1[::-1]      

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                return False
        return True
            

                   



        