class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        string_list = []
        string_list[:] = A
        n = len(A)
        count_1 = 0
        max_length = 0
        i=0
        for i in range(0, n):
            count_1 = count_1 + 1
            if string_list[i] == '0':
                for j in range(i + 1, n):
                    if string_list[j] == '1':
                        count_1 = count_1 + 1
                        if max_length < count_1:
                            max_length = count_1
                            count_1 = 0
                            i = j

        if max_length == 0:
            return count_1
        else:
            return max_length


if __name__ == '__main__':
    A = "11011011"
    length = Solution().solve(A)
    print(str(length))
