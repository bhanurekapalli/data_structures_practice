class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        size = len(A)
        A.sort()
        for i in range(0, size - 1):
            if A[i] == A[i + 1]:
                continue
            if A[i] == size - i - 1:
                return 1
        if A[size - 1] == 0:
            return 1
        return -1


if __name__ == '__main__':
    A = [2,2,5,6]
    is_noble = Solution().solve(A)
    print(str(is_noble))
