n=int(input("enter n no's:"))
ar=list(map(int,input().split()))
t=int(input("enter the t no:"))
for i in range(n):
    if ar[i]==t:
        print("found at",i )
        break
#else:
   # print("Not found")
