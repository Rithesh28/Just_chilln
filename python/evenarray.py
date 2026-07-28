arr=list(map(int,input().split()))
c=0
for i in range(0,len(arr)):
    if arr[i]%2==0:
        c+=1
print(c)