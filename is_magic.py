class Solution:
    # @param A : integer
    # @return an integer
    def sum_of_digits(self,A):
        if A<10:
            return A
        else:
            n=int(A%10)
            A=int(A/10)
            return n+self.sum_of_digits(A)
    def solve(self, A):
        sum_of_all=self.sum_of_digits(A)
        while sum_of_all>9:
            sum_of_all=self.sum_of_digits(sum_of_all)

        if sum_of_all==1:
            return 1
        else:
            return 0


if __name__ == '__main__':
    A = 83557
    is_A_magic = Solution().solve(A)
    print(str(is_A_magic))
