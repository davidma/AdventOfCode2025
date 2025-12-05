#!/usr/bin/python3

## ======================================================
## For timing statistics
import time
stime = time.perf_counter()
## ======================================================

file = open('input.txt','r');

result = 0
range_list = []
candidates = []

## Go through file, line by line - add to the appropriate datastructure
for line in file:

    line = line.strip()

    ## Storing all values takes up too much memory - just store start/end as a list of tuples
    if any(c in "-" for c in line):
        range_list.append(tuple(map(int,line.split('-'))))

    ## IDs can just go into a list
    elif(line.isdigit()):
        candidates.append(int(line))

## Then just check each ID against the list of range tuples - break at first match
for id in candidates:
    for (start,end) in range_list:
        if (id >= start and id <= end):
            result += 1 
            break

## Heres the result
print ('Result is: ' + str(result))

## ======================================================
## Time taken
etime = time.perf_counter()
print (f"[TIMER: Ran in {(etime - stime)*1000:0.4f} ms]")
## ======================================================
