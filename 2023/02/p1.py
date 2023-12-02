cubes = {
    "red":12,
    "green":13,
    "blue":14
}
inputFile = open("input.txt","r")
sum = 0
gameId = 1
for games in inputFile:
    print(gameId)
    cubeSets = games[8:].strip().replace(":","").split("; ")
    isValid = True
    for cubeSet in cubeSets:
        for cubesDrawn in cubeSet.split(", "):
            nCubes = int(cubesDrawn.split()[0])
            cube = cubesDrawn.split()[1]
            if nCubes > cubes[cube]:
                isValid = False
                break
    print(isValid)
        
    if isValid:
        sum+=gameId
    gameId+=1
print(sum)
    