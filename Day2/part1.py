file = open('input.txt','r');

result = 0

## Go through file, line by line (theres only one...)
for line in file:
    line = line.strip()

    ## split the line into the ranges
    range_list = line.split(',')

    for c_range in range_list:
        (s,f) = c_range.split('-')

        ## start and end of current range
        curr = int(s)
        finish =  int(f)

        while curr <= finish:
            cstring = str(curr)
            
            ## fold the number in half - if they match, its invalid
            if len(cstring) % 2 == 0:
                 if cstring[:len(cstring) // 2] * 2 == cstring:
                     result += curr
            
            curr += 1

print ('Result is: ' + str(result))