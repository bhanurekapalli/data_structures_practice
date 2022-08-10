class Solution:
    # @param A : tuple of integers
    # @return an integer
    def binaryToDecimal(self, binary):

        binary1 = binary
        decimal, i, n = 0, 0, 0
        while (binary != 0):
            dec = binary % 10
            decimal = decimal + dec * pow(2, i)
            binary = binary // 10
            i += 1
        return decimal

    def singleNumber(self, A):
        number = 0
        for i in range(0, 32):
            c = 0
            for x in A:
                c = c + x >> i
            number = number + (c % 3) * 10 ** i
        return self.binaryToDecimal(number)

if __name__=='__main__':
    A=[1, 2, 4, 3, 3, 2, 2, 3, 1, 1]
    print(str(Solution().singleNumber(A)))