n=int(input("Enter a number:"))
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n//=10
print(rev)
#for i in range(n,0,-1):
#    print(i)