#factorial
class Solution:
    def factorial (self, N):
        if N == 0 or N == 1:
            return 1
        else:
            result = 1
            for i in range(2, N + 1):
                result *= i
            return result
#fibonacci number 
class Solution(object):
    def fib(self, n):
        if(n==0):
            return 0 
        elif(n==1):
            return 1
        else:
            a=0 
            b=1 
            for i in range(2,n+1): 
             c=a+b 
             a=b 
             b=c 

            return c


