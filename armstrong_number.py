def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    n = int(input())
    i = 1
    rm = 0
    while i <= n:
        sum_of_cubes = 0
        temp = i
        while temp > 0:
            rm = int(temp % 10)
            sum_of_cubes = sum_of_cubes + rm ** 3
            temp = int(temp / 10)
        if sum_of_cubes == i:
            print(str(i))
        i = i + 1
    return 0


if __name__ == '__main__':
    main()
