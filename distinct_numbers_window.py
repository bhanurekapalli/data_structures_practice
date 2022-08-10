class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def dNums(self, A, B):
        N = len(A)
        hashm = {}
        res = []
        for j in range(B):
            if A[j] not in hashm:
                hashm[A[j]] = 1
            else:
                hashm[A[j]] += 1

        res.append(len(hashm))

        for i in range(N - B):
            if A[i] in hashm:
                if hashm[A[i]] == 1:
                    del hashm[A[i]]
                else:
                    hashm[A[i]] -= 1
            if A[i + B] not in hashm:
                hashm[A[i + B]] = 1
            else:
                hashm[A[i + B]] += 1

            res.append(len(hashm))

        return res

if __name__ == '__main__':
    A = [1, 2, 1, 3, 4, 3]
    B = 3
    print(Solution().dNums(A, B))
