class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def addBinary(self, A, B):
        list_a = []
        list_a[:] = A
        n_a = len(A)
        list_b = []
        list_b[:] = B
        n_b = len(B)
        x = n_a - 1
        y = n_b - 1
        carry_forward = 0
        result_string = ""

        while x >= 0 and y >= 0:
            sum_temp = int(list_a[x]) + int(list_b[y]) + carry_forward
            value = int(sum_temp % 2)
            carry_forward = int(sum_temp / 2)
            result_string = str(value)+result_string
            x = x - 1
            y = y - 1

        if x >= 0:
            for i in range(x, -1, -1):
                sum_temp = int(list_a[i]) + carry_forward
                value = int(sum_temp % 2)
                carry_forward = int(sum_temp / 2)
                result_string = str(value)+result_string
        if y >= 0:
            for i in range(y, -1, -1):
                sum_temp = int(list_b[i]) + carry_forward
                value = int(sum_temp % 2)
                carry_forward = int(sum_temp / 2)
                result_string = str(value)+result_string
        if carry_forward >0:
            result_string=str(carry_forward)+result_string

        return result_string


if __name__ == '__main__':
    A = "11"
    B = "1"
    result_binary_sum = Solution().addBinary(A, B)
    print(result_binary_sum)
