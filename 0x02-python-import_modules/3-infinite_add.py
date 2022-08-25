#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    add = 0
    lent = len(sys.argv)

    for i in range(1, lent):
        add += int(sys.argv[i])
    print("{}".format(add))
