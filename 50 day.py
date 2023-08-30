class Solution:
    def leftRotate(self, arr, n, d):
         arr[0:]=arr[d:]+arr[:d]
