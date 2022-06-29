class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        difference = None
        for i in range(0, len(A) - 1):
            if difference is None:
                difference = A[i + 1] - A[i]
            else:
                if A[i + 1] - A[i] != difference:
                    return 0
        return 1


if __name__ == "__main__":
    A = [3, 1, 5]
    is_arithmatic = Solution().solve(A)
    print(str(is_arithmatic))
