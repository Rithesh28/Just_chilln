arr = list(map(int, input("Enter numbers: ").split()))
count = 0
for num in arr:
    if num % 2 == 0:
        count += 1
print("Number of even elements:", count)