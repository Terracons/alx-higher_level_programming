#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    list_n = int(len(sys.argv))
    if list_n < 2:
        print("{:d} arguments.".format(list_n-1))
    elif list_n == 2:
        print("{:d} argument:".format(list_n-1))
        print("{:d}: {:s}".format((list_n-1), (sys.argv[list_n-1])))
    elif list_n > 2:
        print("{:d} arguments:".format(list_n-1))
        for i in range(list_n-1):
            print("{:d}: {:s}".format((i+1), (sys.argv[i+1])))
