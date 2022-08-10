class Solution:
    # @param A : list of list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @param D : list of integers
    # @param E : list of integers
    # @return a list of integers
    def solve(self, A, B, C, D, E):
        rows = len(A)
        cols = len(A[0])

        pf = [[0] * cols for i in range(rows)]

        # row wise pf
        for i in range(rows):
            prev = A[i][0]
            pf[i][0] = A[i][0]
            for j in range(1, cols):
                pf[i][j] = prev + A[i][j]
                prev = pf[i][j]

        # col wise pf
        for j in range(cols):
            prev = pf[0][j]
            for i in range(1, rows):
                pf[i][j] = prev + pf[i][j]
                prev = pf[i][j]

        # submatrix sum calculation

        res = []
        for q in range(len(B)):
            a1, b1 = B[q] - 1, C[q] - 1

            a2, b2 = D[q] - 1, E[q] - 1

            total_sum = pf[a2][b2]  # BOTTOM-RIGHT SUM  (TOTAL PF)

            # removing top part
            if a1 > 0:
                total_sum -= pf[a1 - 1][b2]

            # removing left part
            if b1 > 0:
                total_sum -= pf[a2][b1 - 1]

            # neutralizing the extra removed part
            if a1 > 0 and b1 > 0:
                total_sum += pf[a1 - 1][b1 - 1]

            res.append(total_sum % (10 ** 9 + 7))

        return res

if __name__=='__main__':
    A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
    B = [1, 2]
    C = [1, 2]
    D = [2, 3]
    E = [2, 3]
    print(Solution().solve(A,B,C,D,E))