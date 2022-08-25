#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    l = int(len(sys.argv))
    if l < 2:
        print("{:d} arguments.".format(l-1))
    elif l == 2:
        print("{:d} argument:\n".format(l-1))
        print("{:d}: {}".format((l-1), (sys.argv[l-1])))
    elif l > 2:
        print("{:d} arguments:\n".format(l-1))
        for i in range(l-1):
            print("{:d}: {}".format((i+1), (sys.argv[i+1]))) 
