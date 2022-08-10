class Solution:
    def firstMissingPositive(self,A):
        n=len(A)
        if n==1 and A[0]==1:
            return n+1
        present_array=[0]*(n+2)
        for i in range(0,n):
            if A[i]>0 and A[i]<n+1:
                present_array[A[i]]=1
        for i in range(1,n+2):
            if present_array[i]==0:
                return i


if __name__=='__main__':
    A=[1,2,4,5,6,3]
    print(str(Solution().firstMissingPositive(A)))