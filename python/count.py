s = input("Enter a string:")
count = 0
inside_word=False
for i in range(len(s)):

#   if s[i] == " " and s[i-1]!=" ":
#       count += 1
    
    if s[i]!=" ":
        inside_word=True
    elif inside_word:
        count+=1
        inside_word=False
if inside_word:
    count+=1
print(count) 