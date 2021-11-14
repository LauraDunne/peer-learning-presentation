def print_sequence():
    num = int(input("Input number here: "))

    print ('Series is: ', 0, ", ", 1, sep = "", end = "")

    i = 2
    a = 0
    b = 1

    while i < num:
        fib = b+a
            
        print (',', fib, end="")
        a = b
        b = fib
        i += 1

if __name__ == '__main__':
    print_sequence()
