class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        start = 0
        end = A
        sqrt = 0
        while start <= end:
            mid = int((start + end) / 2)
            sqrt = mid
            if mid * mid == A:
                break
            elif mid * mid < A:
                start = mid + 1
            else:
                end = mid - 1
        if sqrt * sqrt == A:
            return sqrt
        else:
            return -1


if __name__ == '__main__':
    A = 16
    root = Solution().solve(A)
    print(str(root))
