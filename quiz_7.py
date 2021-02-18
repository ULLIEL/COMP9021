# COMP9021 19T3 - Rachid Hamadi
# Quiz 7 *** Due Thursday Week 9
#
# Randomly generates a grid of 0s and 1s and determines
# the maximum number of "spikes" in a shape.
# A shape is made up of 1s connected horizontally or vertically (it can contain holes).
# A "spike" in a shape is a 1 that is part of this shape and "sticks out"
# (has exactly one neighbour in the shape).


from random import seed, randrange
import sys


dim = 10


def display_grid():
    for row in grid:
        print('   ', *row) 


# Returns the number of shapes we have discovered and "coloured".
# We "colour" the first shape we find by replacing all the 1s
# that make it with 2. We "colour" the second shape we find by
# replacing all the 1s that make it with 3.
def colour_shapes():
    colour_num = 1
    shapes =[]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                colour_num = colour_num + 1
                shape = dfs(grid,[i,j])
                shapes.append(shape)
                for s in shape :
                    grid[s[0]][s[1]]=0

    return shapes


def dfs(grid,start):
    visited,stack = [],[start]
    valid_range = [0,1,2,3,4,5,6,7,8,9]
    while stack:
        vertex = stack.pop()
        if vertex[0] in valid_range and vertex[1] in valid_range and vertex not in visited:
            visited.append(vertex)
            if vertex[0]+1 in valid_range and grid[vertex[0]+1][vertex[1]] == 1 and [vertex[0]+1,vertex[1]] not in visited:
                stack.append([vertex[0]+1,vertex[1]])                      
            if vertex[0]-1 in valid_range and grid[vertex[0]-1][vertex[1]] == 1 and [vertex[0]-1,vertex[1]] not in visited:
                stack.append([vertex[0]-1,vertex[1]]) 
            if vertex[1]+1 in valid_range and grid[vertex[0]][vertex[1]+1] == 1 and [vertex[0],vertex[1]+1] not in visited:
                stack.append([vertex[0],vertex[1]+1]) 
            if vertex[1]-1 in valid_range and grid[vertex[0]][vertex[1]-1] == 1 and [vertex[0],vertex[1]-1] not in visited:
                stack.append([vertex[0],vertex[1]-1])

    return visited
                
def max_number_of_spikes(nb_of_shapes):
    valid_range = [0,1,2,3,4,5,6,7,8,9]
    num_of_spikes = set()
    global grid
    for item in nb_of_shapes:
        grid = [[0 for _ in range(dim)] for _ in range(dim)]
        num = 0
        for i in item:
            grid[i[0]][i[1]] = 1            

        for row in valid_range:    
            for column in valid_range:
                if grid[row][column] == 1:
                    near_num = 0
                    if row + 1 in valid_range and column in valid_range and grid[row+1][column] == 1 :
                        near_num += 1
                    if row - 1 in valid_range and column in valid_range and grid[row-1][column] == 1 :
                        near_num += 1
                    if row in valid_range and column + 1 in valid_range and grid[row][column+1] == 1:
                        near_num += 1
                        
                    if row in valid_range and column - 1 in valid_range and grid[row][column-1] == 1 :
                        near_num += 1

                    if near_num == 1:
                        num += 1
        num_of_spikes.add(num)

    if num_of_spikes:
        return max(num_of_spikes)
    else:
        return 0

        
        
    


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
nb_of_shapes = colour_shapes()
print('The maximum number of spikes of some shape is:',
      max_number_of_spikes(nb_of_shapes)
     )
