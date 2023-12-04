inputFile = open("input.txt","r")

cards = inputFile.readlines()
nCards = [[1]*len(cards)][0]
for i in range(len(cards)):
    card = cards[i]
    winningNums = card.strip().split(": ")[1].split(" | ")[0].split(" ")
    playedNums = card.strip().split(": ")[1].split(" | ")[1].split(" ")
    nVinti = 0
    for num in winningNums:
        if  num.isdigit() and num in playedNums:
            nVinti += playedNums.count(num)
    for j in range(nVinti):
        nCards[i+j+1]+=1*nCards[i]
    nVinti = 0
print(sum(nCards))