str = "olilO"
str = str.lower()
n = len(str)
i = 0
j = n-1
ans = True
while i<j:
    if str[i] != str[j]:
        ans = False
        print("not palindrome")
        break
    i += 1
    j -= 1
        
if ans == True:
    print("palindrome")