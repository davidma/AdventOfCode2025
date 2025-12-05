#!/usr/bin/python3

## ======================================================
## For timing statistics
import time
stime = time.perf_counter()
## ======================================================

file = open('input.txt','r');

result = 0
range_list = []

## Go through file, line by line - add to the appropriate datastructure
for line in file:

    line = line.strip()

    ## Storing as a set takes up too much memory - just store start/end as a list of tuples
    if any(c in "-" for c in line):
        range_list.append(tuple(map(int,line.split('-'))))

## Sort the ranges on the first element
range_list.sort(key=lambda x: x[0])

## To store our fixed ranges
all_ids = []

## Try to fix the range list to remove overlaps by adjusting starts/ends
for (c_start,c_end) in range_list:

    ## if it already exists, skip it
    if (c_start,c_end) in all_ids:
        continue

    ## Need to check if c_start or c_end is inside an existing range
    for (start,end) in all_ids:

        ## if c_start is in a range, move it to after end of that range
        if start <= c_start <= end:
            c_start = end+1

        ## if c_end is in a range, move it to before start of that range
        if start <= c_end <= end:
            c_end = start-1

    ## this will not be true if the c_range was fully contained in an existing range already
    ## in which case we dont bother adding or procesing it
    if c_start <= c_end:
        all_ids.append((c_start,c_end))

        ## addtionally - add the size of range to the results
        result += c_end - c_start + 1

## Heres the final result
print ('Result is: ' + str(result))

## ======================================================
## Time taken
etime = time.perf_counter()
print (f"[TIMER: Ran in {(etime - stime)*1000:0.4f} ms]")
## ======================================================
