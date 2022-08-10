class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        _i = 0
        _j = -1
        n = len(A)
        m = len(A[0])
        i = 0
        j = m-1
        while i < n and j>=0:
            if A[i][j] == B:
                _i = i+1
                _j = j+1
                break
            else:
                if B > A[i][j]:
                    i = i + 1
                else:
                    j = j - 1
        return _i * (1009) + _j


if __name__ == '__main__':
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(str(Solution().solve(A, 2)))
