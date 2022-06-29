class Solution:
    # @param A : string
    # @return a strings
    def reverse_str(self, str_a, l, r):
        B = bytearray()
        for i in range(r, l - 1, -1):
            x = ord(str_a[i])
            B.append(x)
        return (str(B.decode()))

    def solve(self, A):
        n = len(A)
        r_str = self.reverse_str(A, 0, n - 1)
        print(r_str)
        l = 0
        r = 0
        ans = ""
        for i in range(0, n):
            if r_str[i] == " " :
                x = self.reverse_str(r_str, l, i - 1)
                print(x)
                ans = ans + x + " "
                l = i + 1

            if i==n-1:
                x = self.reverse_str(r_str, l, i)
                print(x)
                ans = ans + x

        return ans


if __name__ == "__main__":
    A = "hv xdq op qoddptokkz vemmoxrgf ombt gg crulgzfkif"
    reverse_str = Solution().solve(A)
    print(reverse_str)
