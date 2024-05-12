s = "khokho"

n = len(s)
mid = (n//2)
# print(mid)
i = 0
j = mid
ans = 1
while j < n:
    if s[i] != s[j]:
        ans = 0
        break
    
    i += 1
    j += 1
    
print(ans)