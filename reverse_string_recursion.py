def reverse(str):
    n=len(str)
    if n==1:
        return str
    else:
        e=n-1
        return str[n-1]+reverse(str[0:e])
def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    string=input()
    reverse_string=reverse(string)
    print(reverse_string)

    return 0

if __name__ == '__main__':
    main()