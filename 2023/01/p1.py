import string

f = open("input.txt","r")
digits = string.digits
sum = 0
for line in f:
    for char in line:
        if char not in digits:
            line = line.replace(char,"")
    sum += int(line[0]+line[-1])
    
print(sum)