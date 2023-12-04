inputFile = open("input.txt","r")
somma = 0
for line in inputFile:
    winningNums = line.strip().split(": ")[1].split(" | ")[0].split(" ")
    playedNums = line.strip().split(": ")[1].split(" | ")[1].split(" ")
    print(winningNums)
    print(playedNums)
    nVinti = 0
    for num in winningNums:
        if  num.isdigit() and num in playedNums:
            nVinti += playedNums.count(num)
    if nVinti > 0:
        vincita = pow(2,nVinti-1)
        somma+=vincita
        print(vincita)
print(somma)
