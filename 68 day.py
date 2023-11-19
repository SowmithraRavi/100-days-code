m = len(matrix)
        n = len(matrix[0])
        cols = []
        rows = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i not in rows:
                        rows.append(i)
                    if j not in cols:
                        cols.append(j)
        for i in rows:
            for j in range(n):
                matrix[i][j] = 0
        for i in cols:
            for j in range(m):
                matrix[j][i] = 0
