s=input("Enter word:")
n=len(s)
is_palindrome=True
for i in range(n//2):
    if s[i]!=s[n-1-i]:
        is_palindrome=False
if is_palindrome:
    print("Palindrome")
else:
    print("not")