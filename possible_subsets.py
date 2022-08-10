import math


class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self, A):
        A.sort()
        all_subsets = []

        n = len(A)  # at max A = 16
        total_subset = 1 << n
        for i in range(total_subset):
            temp = []
            l = i

            for k in range(n):
                if l & 1 == 1:
                    temp.append(A[k])
                l = l >> 1
            all_subsets.append(temp)

        all_subsets.sort()
        return all_subsets

if __name__=='__main__':
    A=[1,2,3]
    list_subsets=Solution().subsets(A)