#pattern 7
class Solution:
    def printTriangle(self, N):
        for i in range(1, N+1):
            print(" " *(N - i), end="")
            print("*" *(2*i - 1))
Output:
    *
   ***  
  *****
 *******
*********

#pattern 8
class Solution:
    def printTriangle(self, N):
        for i in range(N,0,-1):
            print(" " *(N - i), end="")
            print("*" *(2*i - 1))
Output:

*********
 *******
  *****
   ***
    *

