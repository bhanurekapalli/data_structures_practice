class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        count = 0
        n = len(A)
        excel_dict = {"alpha_value":
                          {'A': 1,
                           'B': 2,
                           'C':3,
                           'D':4,
                           'E':5,
                           'F':6,
                           'G':7,
                           'H':8,
                           'I':9,
                           'J':10,
                           'K':11,
                           'L':12,
                           'M':13,
                           'N':14,
                           'O':15,
                           'P':16,
                           'Q':17,
                           'R':18,
                           'S':19,
                           'T':20,
                           'U':21,
                           'V':22,
                           'W':23,
                           'X':24,
                           'Y':25,
                           'Z':26
                           }}
        for i in range(n - 1, -1, -1):
            dict_value = excel_dict["alpha_value"][A[i]]
            count = count + dict_value * (26 ** (n - i - 1))
        return count

if __name__ == "__main__":
    A = "AAA"
    column_value = Solution().titleToNumber(A)
    print(str(column_value))
