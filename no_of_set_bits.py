class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        no_of_set_bits = 0
        while A > 0:
            if A & 1 == 1:
                no_of_set_bits = no_of_set_bits + 1
            A = A >> 1
        return no_of_set_bits


if __name__ == "__main__":
    A = 11
    set_bits = Solution().numSetBits(A)
    print(str(set_bits))
