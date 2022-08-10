class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        C=sorted(A)
        n=len(C)
        i=0
        j=1
        while(i<n and j<n):
            if C[j]-C[i]==B and i!=j:
                return 1
            elif C[j]-C[i]<B:
                j=j+1
            else:
                i=i+1
        return 0
if __name__=='__main__':
    A=[1,5,3]
    k=2
    ans=Solution().diffPossible(A,k)
    print(str(ans))
