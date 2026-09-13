a="Hello"
b="Hi"
#a,b=b,a
a = a + b
b = a[:len(a)-len(b)]
a = a[len(b):]
print(a)
print(b)