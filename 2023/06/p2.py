inputText = open("input.txt","r")

time = int(inputText.readline().strip().split(":")[1].replace(" ",""))
distance = int(inputText.readline().strip().split(":")[1].replace(" ",""))
nPossibili = 1
v = time//2
d = time-v
j=0
while v*d>distance:
    j+=1
    v-=1
    d+=1
j*=2
if not time%2:
    j-=1
nPossibili*=j
print("-----------")
print(nPossibili)