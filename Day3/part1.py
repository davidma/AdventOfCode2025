#!/usr/bin/python3

## ======================================================
## For timing statistics
import time
stime = time.perf_counter()
## ======================================================

file = open('input.txt','r');

result = 0

## Go through file, line by line 
for line in file:
    digits = list(map(int,line.strip()))

    ## Find the largest digit in the list, excluding the last digit
    a = max(digits[0:-1])

    ## record the position of that digit
    p = digits.index(a)

    ## find the largest digit to the right of that position
    b = max(digits[p+1:])

    # put the two digits together and add to result
    result += a*10 + b

print ('Result is: ' + str(result))

## ======================================================
## Time taken
etime = time.perf_counter()
print (f"[TIMER: Ran in {(etime - stime)*1000:0.4f} ms]")
## ======================================================
