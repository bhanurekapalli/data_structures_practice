def solution(n):
    d = [0] * 30
    l = 0
    while (n > 0):
        d[l] = n % 2
        n //= 2
        l += 1
    for p in range(1, l-1):
        ok = True
        for i in range(0,l-p):
            if d[i] != d[i + p]:
                ok = False
                break
        if ok:
            return p
    return -1
if __name__=='__main__':
    n=955
    print(str(solution(n)))