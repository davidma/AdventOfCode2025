#!/usr/bin/python3

## ======================================================
## For timing statistics
import time
stime = time.perf_counter()
## ======================================================

file = open('input.txt','r');

result = 0

## input has multiple lines of numbers and a single line of operators
numbers = []
operators = []

## Go through file, line by line - add to the appropriate datastructure
## This time, add the whole line as a string - we need the spacing
for line in file:

    if '+' in line:
        operators = line.rstrip('\n')
    else:
        numbers.append(line.rstrip('\n'))

## Iterate through all the lines together, from right to left
## When we reach an operator, thats the time to calculate
nums = []
for i in range(len(operators)-1,-1,-1):

    ## Step 1: make a string of all the appropriate characters in the column
    c_num = ''

    for j in range(len(numbers)):
        c_num += numbers[j][i]
    
    ## Step 2: if its a number, add to list of current problems nums
    ## otherwise, its the gap between problems - reset nums and skip to next col
    if c_num.strip().isnumeric():
        nums.append(int(c_num.strip()))
    else:
        nums = []
        continue

    ## Step 3: if we reach an operator, its the last column of the problem
    ## Combine all the current problems nums using the appropriate operator
    tmpres = 0

    if operators[i] == '+':
        tmpres = nums[0]
        for x in range(1,len(nums)):
            tmpres = tmpres + nums[x]
    
    if operators[i] == '*':
        tmpres = nums[0]
        for x in range(1,len(nums)):
            tmpres = tmpres * nums[x]

    ## Step 4: add subtotal to overall total
    result += tmpres

## Heres the result
print ('Result is: ' + str(result))

## ======================================================
## Time taken
etime = time.perf_counter()
print (f"[TIMER: Ran in {(etime - stime)*1000:0.4f} ms]")
## ======================================================
