#!/usr/bin/python3

## ======================================================
## For timing statistics
import time
stime = time.perf_counter()
## ======================================================

file = open('input.txt','r');

result = 0

for line in file:
    digits = list(map(int,line.strip()))

    start = 0

    ## This can solve part 1 and part 2 - just set to 2 digits instead of 12
    goal_digits = 12  

    ## Going to check (goal_digits) sliding windows - slices of the original list
    for i in range(0,goal_digits):

        # Calc the correct end index for the sliding window
        # we need to leave abs(i + 1 - goal_digits) digits off the end each iteration
        end = len(digits)+i+1-goal_digits

        # search the current sliding window for biggest digit
        curr_digit = max(digits[start:end])

        # Save the new start position including the distance from start (old start position)
        start = digits[start:end].index(curr_digit) + start + 1

        # Add the current digit, in the correct 10s place
        result += curr_digit * (10**((goal_digits - 1)-i))

print ('Result is: ' + str(result))

## ======================================================
## Time taken
etime = time.perf_counter()
print (f"[TIMER: Ran in {(etime - stime)*1000:0.4f} ms]")
## ======================================================