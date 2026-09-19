arr=list(map(int,input("Enter numbers:").split()))
for num in arr:
    if num<2:
        print(num,end=" ")
        continue
    is_prime=True
    for i in range(2,num):
        if num%i==0:
            is_prime=False
            break
    if not is_prime:
        print(num,end=" ")
