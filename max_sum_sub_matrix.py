class Solution:
    # @param A : list of list of integers
    # @return an long
    def solve(self, A):
        rows = len(A)
        cols = len(A[0])
        pf = [[0] * cols for i in range(rows)]

        # row-wise pf
        for i in range(rows):
            prev = A[i][0]
            pf[i][0] = A[i][0]
            for j in range(1, cols):
                pf[i][j] = prev + A[i][j]
                prev = pf[i][j]

        # col-wise pf
        for k in range(cols):
            prev = pf[0][k]
            for i in range(1, rows):
                pf[i][k] = prev + pf[i][k]
                prev = pf[i][k]

        max_sum = float('-inf')
        for x in range(rows):
            for y in range(cols):
                cur_sum = pf[rows - 1][cols - 1]  # br(a2,b2) - fixed since its the max ele of sorted mat

                a1, b1 = x, y
                a2, b2 = rows - 1, cols - 1

                if a1 > 0:
                    cur_sum -= pf[a1 - 1][b2]

                if b1 > 0:
                    cur_sum -= pf[a2][b1 - 1]

                if a1 > 0 and b1 > 0:
                    cur_sum += pf[a1 - 1][b1 - 1]

                max_sum = max(max_sum, cur_sum)
        return max_sum

if __name__=='__main__':
    A=[[1,2,3],[4,5,6],[7,8,9]]
    print(str(Solution().solve(A)))