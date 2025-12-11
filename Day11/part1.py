#!/usr/bin/python3

## ======================================================
## For timing statistics
import time
stime = time.perf_counter()
## ======================================================

result = 0
graph = {}

## add each node to the graph dict, pointing at a list of its adjactent nodes
for line in open('input.txt','r'):
    (node,neighbours) = line.strip().split(':')
    graph[node] = neighbours.split()

## Do BFS of graph, counting paths from YOU to OUT
queue = ['you']

while len(queue) > 0:
    curr = str(queue.pop(0))

    if curr == 'out':
        result += 1
    else:
        for next in graph[curr]:
            queue.append(next)

## Heres the result
print ('Result is: ' + str(result))

## ======================================================
## Time taken
etime = time.perf_counter()
print (f"[TIMER: Ran in {(etime - stime)*1000:0.4f} ms]")
## ======================================================