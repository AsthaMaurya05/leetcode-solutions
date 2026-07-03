class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        ans = False
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i==j:
                    continue
                if arr[i]==2*arr[j] or arr[i]*2 == arr[j]:
                    ans = True
                    break

                
        return ans            
        