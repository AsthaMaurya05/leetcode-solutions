class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        elif n==1 or n==2:
            return 1
        else:
            a=0
            b=1
            c=1

            for i in range(1,n):
                res = a+b+c

                a=b
                b=c
                c=res 
            return b         
        