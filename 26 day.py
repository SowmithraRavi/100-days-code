#pattern 1
Output
1
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
class Solution:
    def printTriangle(self, N):
        for i in range(1,N+1):
            for j in range(1, i + 1):
                print(j, end=" ")
            print()
#pattern 2
output
1
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5
class Solution:
    def printTriangle(self, N):
        for i in range(1,N+1):
            for j in range(i):
                print(i, end=" ")
            print()
#pattern 3
output
* * * * *
* * * * 
* * * 
* *  
*
class Solution:
    def printTriangle(self, N):
        for i in range(N,0,-1):
            for j in range(i):
                print("*", end=" ")
            print()
#pattern 4
output
1 2 3 4 5
1 2 3 4
1 2 3 
1 2  
1 
class Solution:
    def printTriangle(self, N):
        for i in range(N,0,-1):
            for j in range(1,i+1):
                print(j, end=" ")
            print()
