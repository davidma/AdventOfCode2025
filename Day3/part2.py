file = open('input.txt','r');

result = 0

## Go through file, line by line 
for line in file:
    digits = list(map(int,line.strip()))

    ## Start at the start, right?
    start = 0

    ## This can solve part 1 and part 2 - just set to 2 digits instead of 12
    goal_digits = 12  

    for i in range(0,goal_digits):

        # Absolute hack job to get the correct end index
        if i == goal_digits - 1:
            ## last iteration- use the size of the list
            end = len(digits)
        else:
            ## every other iteration, some negative index offset
            end = -(goal_digits - 1) +  i

        # search the current sliding window
        a = max(digits[start:end])

        # Save the new start position including the distance from start (old start position)
        start = digits[start:end].index(a) + start + 1

        # Add the current digit, in the correct 10s place
        result += a*(10**((goal_digits - 1)-i))

print ('Result is: ' + str(result))