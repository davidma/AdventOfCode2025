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
            
            ## need to check all the substrings from 1 to midway -> (len(cstring) // 2) + 1
            for k in range(1, (len(cstring) // 2) + 1):

                ## Figure out how many pieces of length k exist (and if theres a remainder)
                (num_pieces,remainder) = divmod(len(cstring),k)

                ## Only works if the string splits into a clean number of parts of length k, no remainder
                if remainder == 0: 
                    
                    ## check if the substing repeated k times is the same as the initial string
                    if cstring[:k] * num_pieces == cstring:
                        result += curr

                        ## We can stop checking - its invalid now
                        ## If we dont, we risk double counting
                        break
            
            curr += 1

print ('Result is: ' + str(result))