#!/usr/bin/python3

## ======================================================
## For timing statistics
import time
stime = time.perf_counter()
## ======================================================

result = 0

nodes = []
rectangles = []

## add each (x,y) point from file to a list
for line in open('input.txt','r'):
    nodes.append(tuple(map(int,line.strip().split(','))))

## calculate all the unique rectangle sizes
for node_a in nodes:
    for node_b in nodes:

        ## we can skip rectangles of size 1
        if node_a == node_b:
            continue
        else:
            x2 = max(node_a[0],node_b[0])
            x1 = min(node_a[0],node_b[0])
            y2 = max(node_a[1],node_b[1])
            y1 = min(node_a[1],node_b[1])

            ## length/height are inclusive, so add one to the diffs
            area = ((x2 - x1) + 1) * ((y2 - y1) + 1)

            rectangles.append((x1,y1,x2,y2,area))

## Sort based on calculated sizes
rectangles = sorted(rectangles,key=lambda x: x[4], reverse=True)

## Size of the largest rectangle we found
result = rectangles[0][4]

## Heres the result
print ('Result is: ' + str(result))

## ======================================================
## Time taken
etime = time.perf_counter()
print (f"[TIMER: Ran in {(etime - stime)*1000:0.4f} ms]")
## ======================================================