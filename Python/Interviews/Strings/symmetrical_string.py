s = "abcab"

n = len(s)
if n%2==0:
    mid = (n//2)
else:
    mid = (n//2) +1
# print(mid)
j = mid
i = 0
ans = 1
while j < n and i < mid:
    if s[i] != s[j]:
        print(s[i],s[j],i,j)
        ans = 0
        break
    
    i += 1
    j += 1
    
print(ans)