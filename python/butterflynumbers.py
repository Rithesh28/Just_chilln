n = int(input())

for i in range(n, 0, -2):
    for j in range(n-i):
        print(" ", end="")

    for j in range(1, i+1):
        print(j, end=" ")

    print()

for i in range(3, n+1, 2):
    for j in range(n-i):
        print(" ", end="")

    for j in range(1, i+1):
        print(j, end=" ")

    print()