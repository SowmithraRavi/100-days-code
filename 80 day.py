class Solution:
    def findTwoElement( self,arr, n): 
        n = len(arr) 
        hash = [0] * (n + 1) 
        for i in range(n):
            hash[arr[i]] += 1
        repeat, miss = -1, -1
        for i in range(1, n + 1):
            if hash[i] == 2:
                repeat= i
            elif hash[i] == 0:
                miss = i

            if repeat != -1 and miss != -1:
                break
        return [repeat, miss]
