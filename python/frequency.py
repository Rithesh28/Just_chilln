string1=input("Enter a word:\n")
c=[]

for i in range(len(string1)):
    if string1[i] not in c:
        c.append(string1[i])
#print(c)
for i in range(len(c)):
    count=0
    #positions=[]
    for j in range(len(string1)):
        if c[i]==string1[j]:
            count+=1
            #positions.append(j)
    if count>0:
        print(c[i],":",count)