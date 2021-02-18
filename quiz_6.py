# COMP9021 19T3 - Rachid Hamadi
# Quiz 6 *** Due Thursday Week 8
#
# Randomly fills an array of size 10x10 with 0s and 1s, and outputs the size of
# the largest parallelogram with horizontal sides.
# A parallelogram consists of a line with at least 2 consecutive 1s,
# with below at least one line with the same number of consecutive 1s,
# all those lines being aligned vertically in which case the parallelogram
# is actually a rectangle, e.g.
#      111
#      111
#      111
#      111
# or consecutive lines move to the left by one position, e.g.
#      111
#     111
#    111
#   111
# or consecutive lines move to the right by one position, e.g.
#      111
#       111
#        111
#         111


from random import seed, randrange
import sys


dim = 10


def display_grid():
    for row in grid:
        print('   ', *row)


def check_link(row,column,length):
    if column+length > 10:
        return False
    elif column < 0:
        return False
    else:
        sum = 0
        for plus in range(length):
            sum = sum + grid[row][column+plus]
        if sum == length:
            return True
        else:
            return False


def find_parallelogram_mid(i,j,length):
    max_size = 0
    for column in range(j,dim):
        size = 0
        result_of_first_line = check_link(i,column,length)
        result_of_second_line = check_link(i+1,column,length)
        if result_of_first_line == True and result_of_second_line == True:
            size = 2*length
            for row in range(i+2,dim):
                re = check_link(row, column, length)
                if re:
                    size = size+length
                else:
                    break
        if size > max_size:
            max_size = size
    return max_size


def find_parallelogram_right(i,j,length):
    max_size = 0
    for column in range(j,dim):
        size = 0
        result_of_first_line = check_link(i,column,length)
        result_of_second_line = check_link(i+1,column+1,length)
        if result_of_first_line == True and result_of_second_line == True:
            size = 2*length
            for row in range(i+2,dim):
                re = check_link(row, column+(row-i), length)
                if re:
                    size = size+length
                else:
                    break
        if size > max_size:
            max_size = size
    return max_size


def find_parallelogram_left(i,j,length):
    max_size = 0
    for column in range(j,dim):
        size = 0
        result_of_first_line = check_link(i,column,length)
        result_of_second_line = check_link(i+1,column-1,length)
        if result_of_first_line == True and result_of_second_line == True:
            size = 2*length
            for row in range(i+2,dim):
                re = check_link(row, column-(row-i), length)
                if re:
                    size = size+length
                else:
                    break
        if size > max_size:
            max_size = size
    return max_size



def find_max(a,b,c):
    if a>b:
        if a>c:
            return a
        else:
            return c
    else:
        if b>c:
            return b
        else:
            return c



def size_of_largest_parallelogram():
    size = 0
    length = 0
    for length in range(2,11):
        for i in range(dim-1):
            max_right = find_parallelogram_right(i,0,length)
            max_left = find_parallelogram_left(i,0,length)
            max_mid = find_parallelogram_mid(i,0,length)
            max = find_max(max_mid,max_left,max_right)
            if max > size:
                size = max
    return size



# POSSIBLY DEFINE OTHER FUNCTIONS


try:

    for_seed, density = (int(x) for x in input('Enter two integers, the second '
                                               'one being strictly positive: '
                                              ).split()
                    )
    if density <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[int(randrange(density) != 0) for _ in range(dim)]
            for _ in range(dim)
       ]
print('Here is the grid that has been generated:')
display_grid()
size = size_of_largest_parallelogram()
if size:
    print('The largest parallelogram with horizontal sides '
          f'has a size of {size}.'
         )
else:
    print('There is no parallelogram with horizontal sides.')

