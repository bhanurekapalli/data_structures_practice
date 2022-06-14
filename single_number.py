class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        x = A[0]
        n = len(A)
        for i in range(1, n):
            x = x ^ A[i]

        return x


if __name__ == "__main__":
    A = [1, 2, 2, 3, 1]
    single_number = Solution().singleNumber(A)
    print(str(single_number))
