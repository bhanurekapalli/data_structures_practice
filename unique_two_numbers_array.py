class Solution:
    # @param A : list of integers
    # @return a list of integers
    def check_bit(self, pos, X):
        if X >> pos & 1 == 1:
            return True
        return False

    def solve(self, A):
        value = A[0]
        n = len(A)
        for i in range(1, n):
            value = value ^ A[i]
        pos = -1
        for i in range(0, 32):
            if self.check_bit(i, value):
                pos = i
                break
        _set = 0
        _unset = 0
        for i in range(0, n):
            if self.check_bit(pos, A[i]):
                _set = _set ^ A[i]
            else:
                _unset = _unset ^ A[i]
        return sorted([_set, _unset])

if __name__=='__main__':
    A=[1, 2, 3, 1, 2, 4]
    print(Solution().solve(A))
