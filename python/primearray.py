arr=list(map(int,input("Enter the array:").split()))
for num in arr:
    if num<2:
        continue
    is_prime=True
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            is_prime=False
            break
    if is_prime:
        print(num,end=" ")
