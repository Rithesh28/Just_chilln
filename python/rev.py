n=int(input("enter n no's:"))
ar=list(map(int,input().split()))
def rev(n,st=0,end=n-1):
    for i in n:  
        while st<end:
            temp=ar[st]
            ar[st]=ar[end]
            ar[end]=temp
            st+=1
            end-=1
    return ar[i]
print(rev(4))


    