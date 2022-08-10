class Solution:
    # @param A : integer
    # @return an integer
    def fibonacci(self,num):
        if num==0:
            return 0
        elif num==1:
            return 1
        else:
            return self.fibonacci(num-1)+self.fibonacci(num-2)
    def findAthFibonacci(self, A):
        return self.fibonacci(A)
if __name__=='__main__':
    A=9
    fibonacci_num=Solution().findAthFibonacci(A)
    print(str(fibonacci_num))