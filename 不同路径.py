#不同路径

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 and n == 0:
            return 0
        Matrix = [[0] * m for i in range(n)]
        for i in range(n):
            for j in range( m):
                if i == 0 and j == 0:
                    Matrix[i][j] = 0
                elif i == 0 and j != 0:         
                    Matrix[i][j] = 1
                elif i != 0 and j == 0:
                    Matrix[i][j] = 1
                else:
                    Matrix[i][j] = Matrix[i - 1][j] + Matrix[i][j - 1]
        return Matrix[n - 1][m - 1]
