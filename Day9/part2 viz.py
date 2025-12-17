#!/usr/bin/python3

import matplotlib.pyplot as plt
from shapely.geometry import Polygon
import matplotlib.animation as animation

fig, ax = plt.subplots()

result = 0

nodes = []
rectangles = []
artists = []

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

outer = Polygon(nodes)
x_o, y_o = outer.exterior.xy

max_area = 0

## Check each rectangle
for x1,y1 in nodes:

    ## we cheat here - this was a point on my final best rectangle
    ## To make the vizualization a manageble length, I fix one corner as this point
    (x2,y2) = (5741,50285)

    (x1,x2) = sorted((x1,x2))
    (y1,y2) = sorted((y1,y2))

    intersect = False

    ## Check if any member of the green polygon is inside the bounds of curr rectangle
    for (gx,gy) in green_tiles:
        if x1 < gx < x2 and y1 < gy < y2:
            intersect = True
            break
        
    if intersect:
        plot1, = ax.plot(x_o,y_o, color="blue")
        plot2, = ax.plot([x1,x1,x2,x2,x1], [y1,y2,y2,y1,y1], color="red")
        artists.append([plot1,plot2])
    else:
        plot1, = ax.plot(x_o,y_o, color="blue")
        plot2, = ax.plot([x1,x1,x2,x2,x1], [y1,y2,y2,y1,y1], color="green")
        artists.append([plot1,plot2])

    ## because rectangles are sorted, first non-intersecting pair wins!
    if not intersect:
        area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
        
        if area > max_area:
            max_area = area
            max_x = [x1,x1,x2,x2,x1]
            max_y = [y1,y2,y2,y1,y1]

## Heres the result
print ('Result is: ' + str(max_area))

plot1, = ax.plot(x_o,y_o, color="blue")
plot2, = ax.plot(max_x, max_y, color="green")
artists.append([plot1,plot2])

ani = animation.ArtistAnimation(fig=fig, artists=artists, interval=10, repeat=False, blit=True)
ani.save(filename="vizualization.gif", writer="pillow")
plt.show()