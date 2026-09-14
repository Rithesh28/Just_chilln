arr=list(map(int,input("Enter array:").split()))
maximum=arr[0]
second=arr[0]
for i in arr:
    if i>maximum:
        second=maximum
        maximum=i
    elif i>second:
        second=i
print(second)