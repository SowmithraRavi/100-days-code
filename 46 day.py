class Solution:

	def print2largest(self,arr, n):
		s=set(arr) 
	    length=len(s) 
	    if(length>1):
	        s=list(s)
	        s.sort() 
	        return s[-2]
	    else:
	        return -1
