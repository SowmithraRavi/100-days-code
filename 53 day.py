#User function Template for python3

class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b,n,m):
        a=set(a)
        b=set(b)
        n=a.union(b) 
        n=list(n)
        n.sort()
        return n
