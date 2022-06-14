class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer

    def solve(self, A, B):
        min_sum = 10 ** 9
        n = len(A)
        for j in range(1, n - 1):
            temp_sum = B[j]
            val_i = 10 ** 9
            val_k = 10 ** 9
            for i in range(0, j):
                if A[i] < A[j]:
                    if val_i > B[i]:
                        val_i = B[i]

            for k in range(j + 1, n):
                if A[k] > A[j] :
                    if val_k > B[k]:
                        val_k = B[k]
            if val_i != 10 ** 9 and val_k != 10 ** 9:
                temp_sum = temp_sum + val_i + val_k
                if temp_sum < min_sum:
                    min_sum = temp_sum

        if min_sum != 10 ** 9:
            return min_sum
        else:
            return -1


if __name__ == '__main__':
    A = [1, 6, 4, 2, 6, 9]
    B = [2, 5, 7, 3, 2, 7]
    minimum_tree_sum = Solution().solve(A, B)
    print(str(minimum_tree_sum))
