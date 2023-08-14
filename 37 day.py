Recursion
#factorial
class Solution:
    def factorial (self, N):
        if(N==0):
            return 1
        else:
            return N * self.factorial(N-1)

#fibonacci
class Solution(object):
    
    def fib(self, n):
        
        if n <= 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            return self.fib(n-1) + self.fib(n-2)
