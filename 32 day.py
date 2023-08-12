class Solution:
    def printTriangle(self, N):
        for i in range(1, 2 * N):
            for j in range(1, 2 * N):
                print(max(abs(N- i), abs(N - j)) + 1, end=" ")
            print()
Output:
4 4 4 4 4 4 4
4 3 3 3 3 3 4
4 3 2 2 2 3 4
4 3 2 1 2 3 4
4 3 2 2 2 3 4
4 3 3 3 3 3 4
4 4 4 4 4 4 4

