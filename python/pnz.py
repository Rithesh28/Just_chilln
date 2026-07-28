n=int(input("enter n no's:"))
ar=list(map(int,input().split()))
c1=0
c2=0
c3=0
for i in range(n):
    if ar[i]>0:
        c1+=1
    elif ar[i]<0:
        c2+=1
    elif ar[i]==0:
        c3+=1
print("positive:",c1)
print("negative:",c2)
print("zero:",c3)
