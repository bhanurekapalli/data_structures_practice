class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        d = 0
        left = 0
        top = 0
        right = A - 1
        bottom = A - 1
        c = []
        for i in range(0, A):
            c.append([0] * A)
        n = 1
        while n <= A * A:
            if d == 0:
                for i in range(left, right + 1):
                    c[top][i] = n
                    n = n + 1
                d = d + 1
                top = top + 1
            if d == 1:
                for i in range(top, bottom + 1):
                    c[i][right] = n
                    n = n + 1
                d = d + 1
                right = right - 1
            if d == 2:
                for i in range(right, left - 1, -1):
                    c[bottom][i] = n
                    n = n + 1
                bottom = bottom - 1
                d = d + 1
            if d == 3:
                for i in range(bottom, top - 1, -1):
                    c[i][left] = n
                    n = n + 1
                left = left + 1
                d = 0
        return c


if __name__ == '__main__':
    A = 5
    spiral_matrix = Solution().generateMatrix(A)
    print(spiral_matrix)
