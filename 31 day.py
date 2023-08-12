class Solution:
    def printTriangle(self, N):
        for i in range(N):
            print('*' * (N - i) + ' ' * (2 * i) + '*' * (N - i))
        for i in range(N):
            print('*' * (i + 1) + ' ' * (2 * (N- i - 1)) + '*' * (i + 1))
Output:
**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********

class Solution:
    def printTriangle(self, N):
        for i in range(N):
            if i == 0 or i == N - 1:
                print('*' * N)
            else:
                print('*' + ' ' * (N - 2) + '*')
Output:
****
*  *
*  *
****

