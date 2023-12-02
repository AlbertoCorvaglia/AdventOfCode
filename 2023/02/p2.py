inputFile = open("input.txt","r")
power = 0
for games in inputFile:
    print(games)
    cubeSets = games[8:].strip().replace(":","").replace(";",",").split(", ")
    reds=[]
    blues=[]
    greens=[]
    for cube in cubeSets:
        if "red" in cube:
            reds.append(int(cube.split()[0]))
        elif "blue" in cube:
            blues.append(int(cube.split()[0]))
        elif "green" in cube:
            greens.append(int(cube.split()[0]))        
    power+=max(reds)*max(blues)*max(greens)
    
print(power)
