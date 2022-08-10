class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def twoSum(self, A, B):
        indexes = []
        n = len(A)
        dict_A=dict()
        for i in range(0,n):
            temp=B-A[i]
            if temp in dict_A:
                indexes.append(dict_A[temp])
                indexes.append(i+1)
                return indexes
            if not A[i] in dict_A:
                dict_A[A[i]]=i+1
        return []

if __name__ == '__main__':
    A = [4, 7, -4, 2, 2, 2, 3, -5, -3, 9, -4, 9, -7, 7, -1, 9, 9, 4, 1, -4, -2, 3, -3, -5, 4, -7, 7, 9, -4, 4, -8]
    B = -3
    list_i = Solution().twoSum(A, B)
    print(list_i)
