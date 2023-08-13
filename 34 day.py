#prime number
class Solution:
    def isPrime (self, N):
        if N <= 1:
            return 0
        if N <= 3:
            return 1
        if N % 2 == 0 or N % 3 == 0:
            return 0
        i = 5
        while i * i <= N:
            if N % i == 0 or N % (i + 2) == 0:
                return 0
            i += 6
        return 1
        if isPrime (self,N):
            print("1")
        else:
            print("0")
      #reverse integer
    class Solution(object):
    def reverse(self, x):
        result = 0
        if x < 0:
            symbol = -1
            x = -x
        else:
            symbol = 1

        while x:
            result = result * 10 + x % 10
            x /= 10

        return 0 if result > pow(2, 31) else result * symbol
        
