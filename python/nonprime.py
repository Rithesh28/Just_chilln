arr=input("Enter the array")
c=[]
count=0
for i in range(0,len(arr)):
    if arr[i]%i!=0:
        c[i]=c[i]+arr[i]
        count+=1
    if count>1:
        print(c[i])