class Solution:
    # @param A : string
    # @return a strings
    def expand(self,A,p1,p2):
        n=len(A)
        while((p1>=0 and p2<n) and (A[p1]==A[p2])):
            p1=p1-1
            p2=p2+1
        start=p1+1
        end=p2
        return p2-p1+1,A[start:end]
    def findMax(self,x,y):
        if x>y:
            return x
        return y
    def longestPalindrome(self, A):
        n=len(A)
        max_len=1
        ans=""
        if n%2!=0:
            last_index=n
            for i in range(0, last_index):
                temp,sub_str=self.expand(A,i,i)
                max_len=self.findMax(max_len,temp)
                if max_len==temp:
                    ans=sub_str
        else:
            last_index=n-1
            for i in range(0, last_index):
                temp, sub_str = self.expand(A, i, i+1)
                max_len=self.findMax(max_len,temp)
                if max_len==temp:
                    ans=sub_str

        return ans


if __name__ == "__main__":
    A = "aaaabaaa"
    sub_str = Solution().longestPalindrome(A)
    print(sub_str)
