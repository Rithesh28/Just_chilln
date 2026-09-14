arr=list(map(int,input("Enter the array:").split()))
maximum=arr[0]
minimum=arr[0]
for i in arr:
    if i>maximum:
        maximum=i
    if i<minimum:
        minimum=i
print(maximum)
print(minimum)
