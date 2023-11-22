class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        
        prev = self.generate(numRows - 1)
        new= [1] * numRows
        
        for i in range(1, numRows - 1):
            new[i] = prev[-1][i - 1] + prev[-1][i]
        
        prev.append(new)
        return prev
        
