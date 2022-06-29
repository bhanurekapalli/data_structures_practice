class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        bits = []
        reverse_number = 0
        if A == 0:
            return reverse_number
        while A > 0:
            bits.append(A % 2)
            A = int(A / 2)
        # print(bits)
        n = len(bits)
        for i in range(0, n):
            x = 1 << (32 - i - 1)
            reverse_number = reverse_number + (bits[i] * x)

        return reverse_number


if __name__ == "__main__":
    A = 2
    reversed_num = Solution().reverse(A)
    print(str(reversed_num))
