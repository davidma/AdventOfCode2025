#!/usr/bin/python3

## ======================================================
## For timing statistics
import time
stime = time.perf_counter()
## ======================================================

result = 0
presents = []
areas = []
trees = []

## the input file is wierd - first half is shapes, so start in shape mode
## we switch to non-shape mode after the first line with 'x' character
shape_mode = True
shape=[]
for line in open('input.txt','r'):

    if 'x' in line:
        shape_mode = False
    
    if shape_mode:
        if '#' in line:
            shape.append([1 if char == '#' else 0 for char in line.strip()])
        elif ':' in line:
            continue
        else:
            area = sum(row.count(1) for row in shape)
            presents.append(shape)
            areas.append(area)
            shape = []
    else:
        (dim,nums) = line.strip().split(':')
        len_height = tuple(map(int,dim.split('x')))
        num_list = list(map(int,nums.split()))
        trees.append((len_height,num_list))

## Todays problem is a trick - rather than doing any complicated packing, we just need
## to check if the given tree area has enough space to hold the area taken up by the 
## required numbers of each gift - no packing algorithm required!

for (lxh,nums) in trees:
    c_area = lxh[0] * lxh[1]

    c_req = 0
    for i,num in enumerate(nums):
        c_req += nums[i] * areas[i]

    if c_req < c_area:
        result += 1

## Heres the result
print ('Result is: ' + str(result))

## ======================================================
## Time taken
etime = time.perf_counter()
print (f"[TIMER: Ran in {(etime - stime)*1000:0.4f} ms]")
## ======================================================