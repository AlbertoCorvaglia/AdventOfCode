inputFile = open("input.txt","r")


inputLines = inputFile.read().split("\n\n")

seedsRanges = [int(n) for n in inputLines[0].split(": ")[1].split()]

items = []
maps = inputLines[1:]
for seed in seedsRanges:
    for i in range(0,len(seedsRanges),2):
     for j in range(seedsRanges[i], seedsRanges[i]+seedsRanges[i+1]):
        item = seed
        for i in range(len(maps)):
            intervalUsed = False
            for interval in maps[i].split("\n")[1:]:
                interval = [int(n) for n in interval.split()]
                source = interval[1]
                dest = interval[0]
                inc = interval[2]
                if item >= source and item < source+inc and not intervalUsed:
                    item = item + dest - source
                    intervalUsed = True
                    break
                
    items.append(item)
print(min(items))