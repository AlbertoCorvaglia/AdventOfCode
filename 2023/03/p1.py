inputFile = open("input.txt","r")


engineSchema = []
speciali = "=%+&$#*-/@"
for line in inputFile:
    engineSchema.append(line.strip())

sum=0
for i in range(len(engineSchema)):
    for j in range (len(engineSchema[i])):
        
        if engineSchema[i][j] in speciali:
            y=i-1
            while y <= i+1:
                x=j-1
                line = engineSchema[y]
                while x <= j+1:
                    if (x >= 0 and x <= len(engineSchema[y])) and (y >= 0 and y <= len(engineSchema)):
                        if line[x].isdigit():
                            start=x
                            
                            while line[start].isdigit() and start>=0:
                                start-=1
                            while x < len(line) and line[x].isdigit():
                                x+=1

                            num=int(line[start+1:x])
                            sum+=num
                    x+=1
                y+=1
                            
print(sum)