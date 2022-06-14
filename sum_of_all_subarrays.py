class Solution:
    # @param A : list of integers
    # @return an long
    def subarraySum(self, A):
        n = len(A)
        _sum = 0
        string=""
        for s in range(0, n):
            _sum=_sum+A[s]
            for e in range(s, n):
                _sum = _sum + A[e]
        return _sum

if __name__ == '__main__':
    A = [2,9,5]
    sum_of_all_sub_arrays = Solution().subarraySum(A)
    print(str(sum_of_all_sub_arrays))
