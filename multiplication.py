def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    n = int(input())
    i = 1
    while i <= 10:
        pstr = str(n) + " * " + str(i) + " = "
        pstr = pstr + str(i * n)
        print(pstr)
        i = i + 1
    return 0


if __name__ == '__main__':
    main()
