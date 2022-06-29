class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        magic_number = 0
        binary_number = ""
        while A > 0:
            binary_number = str(int(A % 2))+binary_number
            A = int(A / 2)
        print(binary_number)
        n = len(binary_number)
        for i in range(0,n):
            x=int(binary_number[i])
            magic_number = magic_number + 5 ** (n - i)*x
        return magic_number

if __name__ == '__main__':
    A = 10
    mg_num = Solution().solve(A)
    print(str(mg_num))
