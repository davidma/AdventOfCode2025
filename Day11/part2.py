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

## Depth-First Search, with cache of previously visited states
def dfs(edges:dict, vertex:str, goal:str, cache:dict):

    ## If we have reached goal vertex, we are done with this branch!
    if vertex == goal:
        return 1
    else: 
        ## Check if this is a dead-end
        if vertex in edges:
            res = 0

            ## Not a dead end, lets continue down the list of edges leading from this node
            for nxt in edges[vertex]:
                if nxt in cache:
                    ## we've done this branch before - just add cached result
                    res += cache[nxt]
                else:
                    ## New branch - we need to recursivly search it
                    res += dfs(edges,nxt,goal,cache)

            ## Cache sum of all results in this branch, so we dont have to calculate it ever again
            cache[vertex] = res
            return res
        else:
            ## Dead-end!!
            return 0 

## Do DFS of graph, first counting paths from SRV to FFT or DAC
pt1a = dfs(graph,'svr','fft',{})
pt1b = dfs(graph,'svr','dac',{})

## Then check paths from FFT to DAC (or vice versa)
pt2a = dfs(graph,'fft','dac',{})
pt2b = dfs(graph,'dac','fft',{})

## Finally, check paths from DAC/FFT to OUT
pt3a = dfs(graph,'dac','out',{})
pt3b = dfs(graph,'fft','out',{})

## Add all these possibilities together
result = pt1a*pt2a*pt3a + pt1b*pt2b*pt3b

## Heres the result
print ('Result is: ' + str(result))

## ======================================================
## Time taken
etime = time.perf_counter()
print (f"[TIMER: Ran in {(etime - stime)*1000:0.4f} ms]")
## ======================================================