class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def power_function(self, A, n,C):
        if A==0:
            return A
        if n == 0:
            return 1
        half_power = self.power_function(A, int(n / 2),C)
        if n % 2 == 0:
            return (int(half_power%C) * int(half_power%C))%C
        else:
            return ((int(half_power%C) * int(half_power%C))%C*A%C)%C

    def pow(self, A, B, C):
        remainder = self.power_function(A, B,C)
        return remainder


if __name__ == '__main__':
    A = -2
    B = 3
    C = 3
    result = Solution().pow(A, B, C)
    print(str(result))
