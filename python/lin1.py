n=int(input("enter n no's:"))
ar=list(map(int,input().split()))
sum=0
for i in range(n):
        sum=sum+ar[i]
avg=sum/n
print(sum)
print(avg)