#pattern 10
class Solution:
    def printTriangle(self, N):
        for i in range(N-1):
            for j in range(i+1):
                print("*",end=" ")
            print()
        for i in range(N):
            for j in range(i,N):
                print("*",end=" ")
            print()
  Output:
* 
* * 
* * * 
* * * * 
* * * * *
* * * *
* * *
* *
*
#pattern 11
class Solution:
    def printTriangle(self, N):
        for i in range(N):
            for j in range(i+1):
                if (i + j) % 2 == 0:
                    print("1", end=" ")
                else:
                    print("0", end=" ")
            print()
Output:
1 
0 1 
1 0 1
0 1 0 1 
1 0 1 0 1
