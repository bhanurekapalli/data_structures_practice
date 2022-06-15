def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    n = int(input())
    # print(str(n))
    i = 0
    a = [0 for x in range(n)]
    while i < n:
        a[i] = int(input())
        sum_of_factors = 0
        j = 1
        while j < a[i]:
            if a[i] % j == 0:
                sum_of_factors = sum_of_factors + j
            j = j + 1
        if sum_of_factors == a[i]:
            print("YES")
        else:
            print("NO")
        i = i + 1
    return 0


if __name__ == '__main__':
    main()
