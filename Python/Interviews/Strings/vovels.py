str = "appLe"
str = str.lower()
vovels = "aeiou"
count = 0
for item in str:

    if item in vovels:
        count += 1
        
print(count)