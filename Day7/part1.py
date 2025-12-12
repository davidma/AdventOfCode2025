#!/usr/bin/python3

## ======================================================
## For timing statistics
import time
stime = time.perf_counter()
## ======================================================

result = 0

## input has multiple lines of numbers and a single line of operators
tree = []

## Go through file, line by line - add to the appropriate datastructure
for line in open('input.txt','r'):
    tree.append(list(line.rstrip('\n')))

## Replace start position with a beam
tree[0] = ['|' if chr=='S' else chr for chr in tree[0]]

## Ho ho ho, descend the tree
for n in range(0, len(tree)-1):

    ## get all the beam positions on current row
    beams = [i for i, v in enumerate(tree[n]) if v == '|']

    ## Now propogate the beams to the next row
    for x in beams:
        if tree[n+1][x] == '^':
            ## We hit a splitter, split the beam
            tree[n+1][x-1] = '|'
            tree[n+1][x+1] = '|'

            result += 1
        else:
            tree[n+1][x] = '|'

## Heres the result
print ('Result is: ' + str(result))

## ======================================================
## Time taken
etime = time.perf_counter()
print (f"[TIMER: Ran in {(etime - stime)*1000:0.4f} ms]")
## ======================================================
