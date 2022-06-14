class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        n = len(A)
        B = []
        b_r = 2 * n - 1
        for i in range(0, b_r):
            B.append([0] * n)
        i=-1
        #for each column start from 0th row
        for column in range(0,n):
            start_row=0
            start_column=column
            b_c=0
            i=i+1
            while start_row<n and start_column>=0:
                B[i][b_c]=A[start_row][start_column]
                print(str(A[start_row][start_column]))
                b_c=b_c+1
                start_row=start_row+1
                start_column=start_column-1
        #for each row, start from n-1 column
        for row in range(1,n):
            start_row=row
            start_column=n-1
            b_c = 0
            i = i + 1
            while start_row<n and start_column>=0:
                B[i][b_c]=A[start_row][start_column]
                b_c=b_c+1
                start_row=start_row+1
                start_column=start_column-1
        return B


if __name__ == '__main__':
    A = [[1,2,3],[4,5,6],[7,8,9]]
    anti_diagonals_matrix = Solution().solve(A)
    print(anti_diagonals_matrix)
