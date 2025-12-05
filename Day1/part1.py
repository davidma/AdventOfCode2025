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

    ## Do the move
    if direction == 'R':
        position = (position + distance) % 100
    else:
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