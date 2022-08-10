class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        _sum = 0
        for i in range(n):
            sum1 = 0
            for j in range(i, n):
                sum1 = (sum1 | A[j])
            _sum = _sum + sum1
        return _sum
