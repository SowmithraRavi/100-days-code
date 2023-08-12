class Solution:
    def printTriangle(self, N):
       
        for i in range(1, N + 1):
            p=65
            for j in range(1, i + 1):
                print(chr(p), end='')
                p+=1
            print()
Output:
A
AB
ABC
ABCD
ABCDE
