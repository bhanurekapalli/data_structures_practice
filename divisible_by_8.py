class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        str_array = A.split()
        n = len(str_array)
        if n <= 3:
            number_to_check = int(A)
        else:
            number_to_check = int(str_array[n - 3]) * (10 ** 2) + int(str_array[n - 2]) * 10 + int(str_array[n - 1])
        if number_to_check % 8 == 0:
            return 1
        return 0


if __name__ == "__main__":
    A = "8164"
    is_divisible_by_8 = Solution().solve(A)
    print(str(is_divisible_by_8))
