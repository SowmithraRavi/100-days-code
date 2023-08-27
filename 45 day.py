
class Solution:
    def sumOfDivisors(self, N):
        sum1 = 0
        for i in range(1, N+ 1):
            sum1 += (N // i) * i
        return sum1
