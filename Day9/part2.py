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
## Small dataset, so just compare all pairs of nodes
for (x1,y1) in nodes:
    for (x2,y2) in nodes:

        ## length/height are inclusive, so add one to the diffs
        area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
        rectangles.append((x1,y1,x2,y2,area))

## Sort based on calculated sizes
rectangles = sorted(rectangles,key=lambda x: x[4], reverse=True)

## OK, for part 2 - we need to check the rectangles to see if contain any part of the green polygon edge - so we make a set of all those points
green_tiles = set()
for i,(xa,ya) in enumerate(nodes):
    (xb,yb) = nodes[(i+1) % len(nodes)]

    ## Vertical line
    if (xa == xb):
        (y1,y2) = sorted((ya,yb))
        for j in range(abs(y2-y1)+1):
            green_tiles.add((xa,y1+j))

    ## Horizontal line
    else:
        (x1,x2) = sorted((xa,xb))
        for j in range(abs(x2-x1)+1):
            green_tiles.add((x1+j,ya))    

## Check each rectangle
for (x1,y1,x2,y2,area) in rectangles:

    (x1,x2) = sorted((x1,x2))
    (y1,y2) = sorted((y1,y2))

    intersect = False
    ## Check if any member of the green polygon is inside the bounds of curr rectangle
    for (gx,gy) in green_tiles:
        if x1 < gx < x2 and y1 < gy < y2:
            intersect = True
            break

    ## because rectangles are sorted, first non-intersecting pair wins!
    if not intersect:
        result = area
        break

## Heres the result
print ('Result is: ' + str(result))

## ======================================================
## Time taken
etime = time.perf_counter()
print (f"[TIMER: Ran in {(etime - stime)*1000:0.4f} ms]")
## ======================================================