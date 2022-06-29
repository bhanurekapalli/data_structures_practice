class Solution:
    # @param A : list of characters
    # @return a list of characters
    def to_upper(self, A):
        n = len(A)
        B = bytearray()
        for i in range(0, n):
            x = ord(A[i])
            if x >= 97 and x <= 122:
                x = x ^ (1 << 5)
                B.append(x)
            else:
                B.append(x)
        return str(B.decode())


if __name__ == '__main__':
    A = "Awq"
    upper_A = Solution().to_upper(A)
    print(upper_A)
