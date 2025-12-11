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
for line in open('input_test.txt','r'):
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

## OK, for part 2 - we need to check the rectangles to see if they are wholey contained inside the green polygon
## We check to see if any part of the green polygon cuts through and of the edges of our rectangle
## The original input file has the nodes in order - so each node connects directly to the next node
for (x1,y1,x2,y2,area) in rectangles:
    for i,(gx1,gy1) in enumerate(nodes):

        if i == len(nodes) - 1:
            j = 0
        else:
            j = i+1

        (gx2,gy2) = nodes[j]

        if area > 20:
            print(x1,y1,x2,y2,area,gx1,gy1,gx2,gy2)

        ## check if the line from gx1,gy1  to gx2,gy2 intersects the rectangle
        ## TODO: fix this

        ## If got this far, we have no intersection,and hence a result
        result = area

## Heres the result
print ('Result is: ' + str(result))

## ======================================================
## Time taken
etime = time.perf_counter()
print (f"[TIMER: Ran in {(etime - stime)*1000:0.4f} ms]")
## ======================================================