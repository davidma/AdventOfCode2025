#!/usr/bin/python3

## ======================================================
## For timing statistics
import time
stime = time.perf_counter()
## ======================================================

result = 0
connection_limit = 1000
nodes = []
distances = []

## add each node from file to a list to the dict
for line in open('input.txt','r'):
    nodes.append(tuple(map(int,line.strip().split(','))))

## calculate all the unique internode distances
for i,node_a in enumerate(nodes):
    for node_b in nodes[i+1:]:
        ## I'm damned if I'm using external libraries....
        eucelidian_distance = ((node_a[0]-node_b[0])**2 + (node_a[1]-node_b[1])**2 + (node_a[2]-node_b[2])**2)**(1/2)
        distances.append((node_a, node_b, eucelidian_distance))

## Every node starts in its own circuit, with a unique circuit_ref
circuit = {}
for circuit_ref,node in enumerate(nodes):
    circuit[node] = circuit_ref

## Now start connecting nodes into larger circuits
for connection_num,(node_a,node_b,c_dist) in enumerate(sorted(distances, key=lambda x: x[2])):

    ## Part 1 - We stop after N connections
    if connection_num >= connection_limit:
        break

    ref_a = circuit[node_a]
    ref_b = circuit[node_b]

    ## if both nodes are already in the same circuit, skip
    if ref_a == ref_b:
        continue

    ## OK, we are trying to connect node_a's circuit and node_b's circuit
    ## We do this by changing the circuit_ref for all nodes in node_b's current circuit_ref to match node_a's circuit_ref
    for c_node,c_ref in circuit.items():
        if c_ref == ref_b:
            circuit[c_node] = ref_a

## Now get the lengths of the resultant circuits
circuit_lengths = {}
for circuit_num in circuit.values():
    if circuit_num in circuit_lengths:
        circuit_lengths[circuit_num] += 1
    else:
        circuit_lengths[circuit_num] = 1

## We want the length of the top three longest circuits      
lengths = sorted(circuit_lengths.values(),reverse=True)
result = lengths[0] * lengths[1] * lengths[2]

## Heres the result
print ('Result is: ' + str(result))

## ======================================================
## Time taken
etime = time.perf_counter()
print (f"[TIMER: Ran in {(etime - stime)*1000:0.4f} ms]")
## ======================================================