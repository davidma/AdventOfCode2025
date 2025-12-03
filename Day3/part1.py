file = open('input.txt','r');

result = 0

## Go through file, line by line 
for line in file:
    digits = list(map(int,line.strip()))

    a = max(digits[0:-1])
    p = digits.index(a)
    b = max(digits[p+1:])

    result += a*10 + b

print ('Result is: ' + str(result))
