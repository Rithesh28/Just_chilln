n = int(input())

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")

    if i == 1:
        print("*")
    elif i == n:
        for j in range(2 * n - 1):
            print("*", end="")
        print()
    else:
        print("*", end="")
        for j in range(2 * i - 3):
            print(" ", end="")
        print("*")

for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end="")

    if i == 1:
        print("*")
    else:
        print("*", end="")
        for j in range(2 * i - 3):
            print(" ", end="")
        print("*")