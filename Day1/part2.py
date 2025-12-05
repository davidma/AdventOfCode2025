#!/usr/bin/python3

## ======================================================
## For timing statistics
import time
stime = time.perf_counter()
## ======================================================

file = open('input.txt','r');

result = 0
position = 50

## Iterate through the steps
for line in file:
    line = line.strip()

    ## First character is the direction, rest is the distance
    direction = line[:1]
    distance  = int(line[1:])

    ## remove additional revolutions, add extra results for passing zero
    while distance >= 100:
        result += 1
        distance -= 100

    if direction == 'R':
        ## add an extra result if we will pass zero
        if position != 0 and position + distance > 100:
            result += 1     
        position = (position + distance) % 100

    else:
        ## add an extra result if we will pass zero
        if position != 0 and position - distance < 0:
            result += 1
        position = (position - distance) % 100

    ## end up on zero - add a result!
    if position == 0:
        result += 1

print ('Result is: ' + str(result))

## ======================================================
## Time taken
etime = time.perf_counter()
print (f"[TIMER: Ran in {(etime - stime)*1000:0.4f} ms]")
## ======================================================