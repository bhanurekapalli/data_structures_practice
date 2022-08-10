# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, C):
    # write your code in Python 3.6
    n=len(S)
    minimum_cost=0
    for i in range(0,n-1):
        if S[i]==S[i+1]:
            S[i].replace(S[i],"")
            minimum_cost=minimum_cost+C[i]
    return minimum_cost
    pass

if __name__=='__main__':
    S="abccbd"
    C=[0,1,2,3,4,5]
    print(str(solution(S,C)))