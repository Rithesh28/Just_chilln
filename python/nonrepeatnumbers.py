arr=list(map(int,input("Enter array:").split()))
c=[]
for i in arr:
    if i not in c:
        c.append(i)

for i in c:
    count=0
    for j in arr:
        if i==j:
            count+=1
    if count==1:
        print(i)
