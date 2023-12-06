inputText = open("input.txt","r")

times =[int(time) for time in inputText.readline().strip().split(":")[1].split()]
dist =[int(d) for d in inputText.readline().strip().split(":")[1].split()]
nPossibili = 1
for i in range(len(times)):
    time = times[i]
    distance = dist[i]
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
    print(j)
    nPossibili*=j
print("-----------")
print(nPossibili)