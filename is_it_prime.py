def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    number = int(input())
    count = 0
    i = 1
    while i < number:
        if number % i == 0:
            count = count + 1
            if count > 2:
                break
        i = i + 1
    if count > 2:
        print("NO")
    else:
        print("YES")
    return 0


if __name__ == '__main__':
    main()
