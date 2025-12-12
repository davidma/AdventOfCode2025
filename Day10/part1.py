#!/usr/bin/python3

## ======================================================
## For timing statistics
import time
stime = time.perf_counter()
## ======================================================

result = 0

lights = []
buttons = []
joltages = []

## read each line into three datastructures
##  - List of goal light states, expressed as a bitmask converted to an int
##  - List of lists of button press results, again expressed as bitmasks in int form
##  - List of joltages, not used for part 1

for line in open('input.txt','r'):
    bits = line.strip().split()

    ## Lights example .##. -> 0110 -> 6 (int)
    lights.append(int(bits[0][1:-1].replace('#','1').replace('.','0'),2))

    ## Joltages are already ints
    joltages.append(bits[-1][1:-1].split(','))

    ## For each button, do the same as lights
    ## So (1,3) for a seq of 4 buttons -> 0101 -> 5 (int)
    b_list = []
    for b_conf in bits[1:-1]:
        b = list(map(int,b_conf[1:-1].split(',')))

        b_mask = ''
        for n in range(len(bits[0][1:-1])):
            if n in b:
                b_mask += '1'
            else:
                b_mask += '0'
            
        b_list.append(int(b_mask,2))
    
    buttons.append(b_list)

## Now iterate through the problems, light by light
for i in range(len(lights)):

    ## Going to BFS through the set of all light combinations
    goal = lights[i]
    b_list = buttons[i]

    seen_states = set()

    ## at the start, theres no lights (0) and no presses
    queue = [(0,0)]

    while len(queue) > 0:
        state,presses = queue.pop(0)
 
        if state not in seen_states:

            ## the first time we see the goal state, we are done - thats the minimum presses
            if state == goal:
                result += presses

            ## Otherwise, record that we've seen this, and continue
            seen_states.add(state)
            presses += 1

            for b in b_list:
                ## Add all the next states to the queue
                ## The result of the current state XOR with the button bitmask
                ## so like, 6 XOR 5 => 0110 XOR 0101 => 0011 => 3
                queue.append((state ^ b, presses))

## Heres the result
print ('Result is: ' + str(result))

## ======================================================
## Time taken
etime = time.perf_counter()
print (f"[TIMER: Ran in {(etime - stime)*1000:0.4f} ms]")
## ======================================================