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
#fibonacci
class Solution(object):
    
    def fib(self, n):
        
        if n <= 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            return self.fib(n-1) + self.fib(n-2)


