def findIndexes(line, value):
    indexes = []
    
    while True:
        if value in line:
            indexes.append(line.index(value))
            line = line.replace(value,"*"*len(value),1)
        else:
            return indexes
    
    
print(findIndexes("twoeightwo2", "two"))