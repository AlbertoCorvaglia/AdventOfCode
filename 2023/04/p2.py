inputFile = open("input.txt","r")
nCards = 0

print(cards)
for line in inputFile:
    cards.append(line)

# for i in range(len(cards)):
#     card = cards[i]
    
#     winningNums = card.strip().split(": ")[1].split(" | ")[0].split(" ")
#     print(winningNums)
#     playedNums = card.strip().split(": ")[1].split(" | ")[1].split(" ")

#     nVinti = 0
#     for num in winningNums:
#         if  num.isdigit() and num in playedNums:
#             nVinti += playedNums.count(num)


# print(cards)