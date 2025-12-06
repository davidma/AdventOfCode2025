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
for line in file:

    line = line.strip()

    if '+' in line:
        operators = line.split()
    else:
        numbers.append(list(map(int,line.split())))

## Theres the same number of problems as operators...
for i in range(0,len(operators)):

    ## pick the first value as our subtotal
    tmpres = numbers[0][i]

    ## then combine it with the values on the other number lines, using the appropriate operator
    for j in range(1,len(numbers)):
        if operators[i] == '+':
            tmpres = tmpres + numbers[j][i]
        if operators[i] == '*':
            tmpres = tmpres * numbers[j][i]

    ## add subtotal to overall total
    result += tmpres

## Heres the result
print ('Result is: ' + str(result))

## ======================================================
## Time taken
etime = time.perf_counter()
print (f"[TIMER: Ran in {(etime - stime)*1000:0.4f} ms]")
## ======================================================
