n=int(input("enter n no's:"))
ar=list(map(int,input().split()))
s=True
for i in range(0,n-1):
    if ar[i] > ar[i+1]:
        s=False
        break
if s==True:
    print("sorted")
else:
    print("not sorted")
    


   
#50 20 5 30