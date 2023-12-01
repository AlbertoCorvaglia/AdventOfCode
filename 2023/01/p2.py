inputFile = open("input.txt","r")

digits = "0123456789"
wordToDigit = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}
def findIndexes(line, value):
    indexes = []
    
    while True:
        if value in line:
            indexes.append(line.index(value))
            line = line.replace(value,"*"*len(value),1)
        else:
            return indexes
    
def toDigit(line):
    orderedNum={}
    for key in wordToDigit.keys():
        if key in line:
            for index in findIndexes(line, key):
                orderedNum.update({index:key})
    for digit in digits:
        if digit in line:
            for index in findIndexes(line, digit):
                orderedNum.update({index:digit})

    parsedDigit = dict(sorted(orderedNum.items())).values()
    res =""
    for digit in parsedDigit:
        if digit in digits:
            res+=digit
            
        elif digit in wordToDigit.keys():
            res+=wordToDigit[digit]
    return res            
                
                
sum = 0            
for line in inputFile:
    num = toDigit(line)[0]+toDigit(line)[-1]
    print(num)
    sum+=int(num)
print(sum)