class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def solve(self, S):
        K=2
        N = len(S)

        # Stores the minimum subsequence
        answer = []

        # Traverse the string S
        for i in range(N):

            # If the stack is empty
            if (len(answer) == 0):
                answer.append(S[i])
            else:

                # Iterate till the current
                # character is less than the
                # the character at the top of stack
                while (len(answer) > 0 and (S[i] < answer[len(answer) - 1]) and (len(answer) - 1 + N - i >= K)):
                    answer = answer[:-1]

                # If stack size is < K
                if (len(answer) == 0 or len(answer) < K):
                    # Push the current
                    # character into it
                    answer.append(S[i])

        # Stores the resultant string
        ret = []

        # Iterate until stack is empty
        while (len(answer) > 0):
            ret.append(answer[len(answer) - 1])
            answer = answer[:-1]

        # Reverse the string
        ret = ret[::-1]
        ret = ''.join(ret)

        # Print the string
        return ret


if __name__=='__main__':
    A="nfqhtxeqoa"
    Solution().solve(A)
