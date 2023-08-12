class Solution:
    def printTriangle(self, N):
        for i in range(1, N + 1):
            for j in range(1, i + 1):
                print(j, end=' ')
            for _ in range(2 * (N - i)):
                print(' ', end=' ')
            for j in range(i, 0, -1):
                print(j, end=' ')
            print()
output:
1                 1
1 2             2 1
1 2 3         3 2 1
1 2 3 4     4 3 2 1
1 2 3 4 5 5 4 3 2 1

class Solution:
    def printTriangle(self, N):
        p=1
        for i in range(N):
            for j in range(i+1):
                print(p,end=" ")
                p+=1
            print()
Output:
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15

