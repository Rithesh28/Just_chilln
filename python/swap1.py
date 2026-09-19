s1=input("Enter a word:")
s2=input("Enter another word:")
#s1, s2=s2, s1
s1=s1+s2
s2=s1[:len(s1)-len(s2)]
s1=s1[len(s2):]
print(s1)
print(s2)