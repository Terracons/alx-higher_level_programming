#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for row in matrix:
            # Loop through the items in the row
            for item in row:
                # input space if not last item
                if row.index(item) != len(row) - 1:
                    endspace = " "
                else:
                    endspace = ""
                # Print  all item in the row
                print("{:d}".format(item), end=endspace)
            print()
