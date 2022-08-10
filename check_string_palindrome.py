class Solution:
    # @param A : string
    # @return an integer
    def check_palindrome(self,str):
        s=0
        e=len(str)-1
        if s>e:
            return 1
        elif str[s]==str[e]:
            return self.check_palindrome(str[1:e])
        else:
            return 0
    def solve(self, A):
        n=len(A)
        is_palindrome=self.check_palindrome(A)
        return is_palindrome
if __name__=='__main__':
    A="malayalam"
    is_palindrome=Solution().solve(A)
    print(str(is_palindrome))