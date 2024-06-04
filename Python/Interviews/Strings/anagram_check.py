list1 = ['silent', 'enlist',"sile", 'inlets', 'tinsel']

str = 'listen'

def check_anag(str, list):
    
    for item in list:
        if sorted(str) == sorted(item):
            print(item, " is anagram")
        else:
            print(item, " is not anagram")

check_anag(str, list1)


def chk_anagram(l,s):
    
    ans = []
    b = []
    for item in l:
        if sorted(item) == sorted(s):
            ans.append(f"{item} is anagram of {s}")
            b.append(True)
        else:
            ans.append(f"{item} is not an anagram of {s}")
            b.append(False)
    return ans,b
    
print(chk_anagram(list1,str))   #returns a tuple with both (ans,b) values
print(chk_anagram(list1,str)[0])    #get only ans[] from tuple (ans,b)
print(chk_anagram(list1,str)[1])    #gett only b[] from tuple (ans,b)

s1 = 'listen'
s2 = 'enlist'
from collections import Counter
print(Counter(s1)== Counter(s2))