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

## We also need to keep track of num of timelines in each col, initially all zero
timelines = [0] * len(tree[0])

## Replace start position with a beam, and add a timeline to that col
s_pos = tree[0].index('S')
tree[0][s_pos] = '|'
timelines[s_pos] += 1

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

            ## update the timelines
            timelines[x-1] += timelines[x]
            timelines[x+1] += timelines[x]
            timelines[x] = 0 
        else:
            tree[n+1][x] = '|'

## Heres the result
result = sum(timelines)

print ('Result is: ' + str(result))

## ======================================================
## Time taken
etime = time.perf_counter()
print (f"[TIMER: Ran in {(etime - stime)*1000:0.4f} ms]")
## ======================================================
