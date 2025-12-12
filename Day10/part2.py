#!/usr/bin/python3

## ======================================================
## For timing statistics
import time
stime = time.perf_counter()
## ====================================================== 

## I havent written this myself - I've relied heavily on other solutions and the Z3 Problem Solver
## Details are at: https://z3prover.github.io/api/html/z3.z3.html
## This makes me feel bad, but I just want to finish this before the heat death of the universe

from z3 import *

result = 0

problems = []

## Parse the input - forget the lights, and keep the buttons/voltages as plain lists of ints
## This (someone elses) code is much more elegant than mine in part 1, but it does the same kind of thing
## Its just written by someone who uses Python a lot more than me! :-)

with open('input.txt', "r") as f:
    for parts in [line.strip().split() for line in f]:
        buttons = [[int(b) for b in button[1:-1].split(",")] for button in parts[1:-1]]
        voltages = [int(v) for v in parts[-1][1:-1].split(",")]
        problems.append([buttons, voltages])

## Iterate through the problem set
for buttons, voltages in problems:

    ## the z3 solver object
    ## This is going to do all the heavy lifting
    solver = Solver()

    ## Create a set of empty variables, one per button - representing the number of button presses
    unknowns = [Int(f"a{n}") for n in range(len(buttons))]

    ## Add the contraint that each button can only be pressed zero or more times
    ## (No negative values for unknowns) 
    for x in unknowns:
        solver.add(x >= 0)

    ## iterate through each voltage in the goal, and make an equation
    for i,v in enumerate(voltages):
        relevant_buttons = []

        ## make a list of the buttons that impact the voltage in position i
        for j,button in enumerate(buttons):
            if i in button:
                relevant_buttons.append(unknowns[j])
        
        ## add an equation => sum(relevant_buttons) = voltage
        #print('>>> Adding contraint: ' + str(Sum(relevant_buttons)) + ' = ' + str(v))
        solver.add(Sum(relevant_buttons) == v)

    total_val = 0

    ## We've got to get the minimal answer - z3 may not return this first time
    ## We'll let it solve, and then add a new constraint to make it try and find a smaller solution
    ## eventually, the new constraint will break the set of equations, and the loop will break 
    ## at this stage, we have already found the minimal solution (if one exists)

    while solver.check() == sat:

        ## try to solve the set of equations, give back results for each unknown
        model = solver.model()

        ## Add up the current best values for all the unknowns in the model
        total_val = sum([model[d].as_long() for d in model])
        
        ## Add a new constraint that trys to make the solver find a lower set of values
        #print('>>> Adding new contraint: ' + str(Sum(unknowns)) + ' < ' + str(total_val))
        solver.add(Sum(unknowns) < total_val)

    ## we've found the minimal set of values, add to result
    result += total_val

## Heres the grand total result
print ('Result is: ' + str(result))

## ======================================================
## Time taken
etime = time.perf_counter()
print (f"[TIMER: Ran in {(etime - stime)*1000:0.4f} ms]")
## ======================================================