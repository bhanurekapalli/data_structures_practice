from functools import cmp_to_key


class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        A = list(map(str, A))

        def compare(num1, num2):
            if num1 + num2 > num2 + num1:
                return -1
            else:
                return 1

        A = sorted(A, key=cmp_to_key(compare))
        if A[0] == '0':
            return 0
        return "".join(A)


if __name__ == '__main__':
    A = [3, 30, 34, 5, 9]
    print(Solution().largestNumber(A))
