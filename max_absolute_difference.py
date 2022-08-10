class Solution:
    # @param A : list of integers
    # @return an integer
    def find_max(self,x,y):
        if x>y:
            return x
        return y

    def find_min(self,x,y):
        if x<y:
            return x
        return y
    def maxArr(self, A):
        max_sum=-10**9
        min_sum=10**9
        max_diff=-10**9
        min_diff=10**9
        n=len(A)
        for i in range(0,n):
            sum=A[i]+i
            diff=A[i]-i
            max_sum=self.find_max(sum,max_sum)
            min_sum=self.find_min(sum,min_sum)
            max_diff=self.find_max(diff,max_diff)
            min_diff=self.find_min(diff,min_diff)
        return self.find_max(max_sum-min_sum,max_diff-min_diff)

if __name__=='__main__':
    A=[1, 3, -1]
    print(str(Solution().maxArr(A)))