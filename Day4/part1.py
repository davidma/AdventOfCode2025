#!/usr/bin/python3

##==============================================================================
## Generic helper functions for working with AdventOfCode Grid data
##
## We store grid data as an array of arrays e.g. grid[0][0] = top left value
##==============================================================================

## Converts a file into a grid, optionally, stored as ints
def populate_grid(file,dtype=''):
    grid_ds = []

    with open(file, 'r') as fh:
        for line in fh:
            if dtype == 'int':
                ## Store the value as an int
                grid_ds.append(list(map(int,line.strip())))
            else:
                ## Store it as a string (default)
                grid_ds.append(list(line.strip()))

    return grid_ds

##  Gets the height of a grid 
def get_height (grid_ds):
    return len(grid_ds)

## gets the width of a grid
def get_width(grid_ds):
    return len(grid_ds[0])

## returns a list of tuples, every node in the grid
def get_all_nodes(grid_ds):
    for x,row in enumerate(grid_ds):
        for y,val in enumerate(row):
               yield (x,y) 

## checks if a point (x,y) is outside the bounds of a grid
def out_of_bounds(x,y,grid_ds):
    if (0 <= x < get_width(grid_ds)) and (0 <= y < get_height(grid_ds)):
        return False
    else:
        return True

## Draw the current state of a grid - useful for debugging
def print_grid(grid_ds):
    for row in grid_ds:
        for val in row:
            print(str(val),end='')
        print()

##==============================================================================
## Problem specific functions from here on....
##==============================================================================

## returns a list of tuples, every node in the grid that is a roll '@'
def get_all_roll_locations(grid_ds):
    for x,row in enumerate(grid_ds):
        for y,val in enumerate(row):
               if grid_ds[x][y] == '@':
                    yield (x,y) 

## Checks is a roll is reachable or not   
def is_reachable_roll(ci,cj,grid_ds,n):

    count = 0

    ## if its not a roll, just give up
    if grid_ds[ci][cj] != '@':
        return False
    
    ## otherwise, check all the neighbours
    else:
        for oi in range(-1,2):
            for oj in range(-1,2):
                if not (out_of_bounds(ci+oi,cj+oj,grid_ds)):
                    if grid_ds[ci+oi][cj+oj] == '@':
                        count += 1

    ## the code above will also count the node itself, so n+1 is max
    if count < n+1:
        return True
    else:
        return False


##==============================================================================
## Main Code starts here
##==============================================================================

## Running total
result = 0 

## Max number of permissable surrounding rolls for roll to be reachable
max_neighbor_rolls = 4

## Load the data into an array of arrays
values = populate_grid('input.txt')

## Get the starting set of roll locations
rolls = list(get_all_roll_locations(values))

## Iterate through every known roll
for (i,j) in rolls:

    ## check if the roll is "reachable" according to problem spec 
    if is_reachable_roll(i, j, values, max_neighbor_rolls):

        ## Update the totals
        result += 1

## All done, print the results
print ('Result is: ' + str(result))