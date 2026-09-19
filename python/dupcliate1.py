a=input("Enter a word:")
c=[]
for i in range(len(a)):
    if a[i] not in c:
        c.append(a[i])
for i in range(len(c)):
    count=0
    position=[]
    for j in range(len(a)):
        if c[i]==a[j]:
            count+=1
            position.append(j)
    if count>0:
        print(c[i],":",position)