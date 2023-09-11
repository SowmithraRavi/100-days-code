class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
        di={} 
        maxlen=0 
        s=0 
        for i in range(n):
            s+=arr[i] 
            if s==k:
                maxlen=max(maxlen,i+1)
            rem=s-k 
            if rem in di:
                length=i-di[rem] 
                maxlen=max(maxlen,length) 
            if s not in di:
                di[s]=i 
                
        return maxlen
        
