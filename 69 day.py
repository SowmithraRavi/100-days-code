class Solution(object):
    def rotate(self, matrix):
        for k in range(len(matrix)):
            for j in range(len(matrix)-1, -1, -1):
                matrix[k].append(matrix[j].pop(0))
        
