class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer
    def findMod(self, A, B):
        value = 1
        n=len(A)
        ans=0
        for i in  range(n-1,-1,-1):
            ans=ans+(int(A[i])%B*value)%B
            value=(10%B*value)%B
        return ans%B
if __name__=="__main__":
    A="36459"
    B=6
    modulus=Solution().findMod(A,B)
    print(str(modulus))
