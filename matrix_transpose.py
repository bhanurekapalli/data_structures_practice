class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def swap(self, x, y):
        temp = x
        x = y
        y = temp
        return x, y

    def solve(self, A):
        n = len(A)
        m = len(A[0])
        B = []
        for i in range(0, m):
            B.append([0] * n)
        for i in range(0, m):
            for j in range(0, n):
                B[i][j]=A[j][i]
        return B

if __name__ == '__main__':
    A = [[1,2], [1,2], [1,2]]
    transpose_matrix = Solution().solve(A)
    print(str(transpose_matrix))
