import sys
class Solution:
    # @param A : tuple of integers
    # @return an integer

    def majorityCandidates(self, A):
        first = sys.maxsize
        second = sys.maxsize
        count1 = 0
        count2 = 0
        for i in range(0, len(A)):
            if first == A[i]:
                count1 += 1
            elif second == A[i]:
                count2 += 1

            elif count1 == 0:
                count1 = count1 + 1
                first = A[i]
            elif count2 == 0:
                count2 = count2 + 1
                second = A[i]
            else:
                count1 = count1 - 1
                count2 = count2 - 1

        return first, second

    def isMajority(self, A, cand1, cand2):
        count1 = 0
        count2 = 0
        n = len(A)
        for i in range(0, n):
            if A[i] == cand1:
                count1 += 1
            if A[i] == cand2:
                count2 += 1
        if count1 > n / 3:
            return cand1
        elif count2 > n / 3:
            return cand2
        else:
            return -1

    def repeatedNumber(self, A):
        first, second = self.majorityCandidates(A)
        print(str(first))
        print(str(second))
        majority = self.isMajority(A, first, second)
        return majority

if __name__ == '__main__':
    A = [1,1,2]
    repeated_number=Solution().repeatedNumber(A)
    print(str(repeated_number))
