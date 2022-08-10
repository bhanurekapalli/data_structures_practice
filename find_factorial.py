class Solution:
    # @param A : integer
    # @return an integer
    def factorial(self,num):
        if num==1:
            return 1
        else:
            return num*self.factorial(num-1)
    def solve(self, A):
        return self.factorial(A)
if __name__=='__main__':
    A=5
    factorial_a=Solution().solve(A)
    print(str(factorial_a))