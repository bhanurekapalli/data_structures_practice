def calculate_prefix_sum(A):
    n = len(A)
    pref = [0] * n
    pref[0] = A[0]
    for i in range(1, n):
        pref[i] = pref[i - 1] + A[i]
    return pref


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer

    def solve(self, A, B):
        pref_sum = calculate_prefix_sum(A)
        # print(pref_sum)
        index = 0
        n = len(A)
        least_avg = pref_sum[n - 1]
        _sum = 0
        for i in range(0, n):
            if i == 0:
                _sum = (pref_sum[B - 1] / B)
            else:
                if (B + i - 1) < n:
                    _sum = ((pref_sum[B + i - 1] - pref_sum[i - 1]) / B)
                else:
                    break
            print(str(_sum) + " for index i:" + str(i))
            if least_avg > _sum:
                least_avg = _sum
                index = i
        return index


if __name__ == '__main__':
    A = [20, 3, 13, 5, 10, 14, 8, 5, 11, 9, 1, 11]
    B = 9
    least_average_index = Solution().solve(A, B)
    print(str(least_average_index))
