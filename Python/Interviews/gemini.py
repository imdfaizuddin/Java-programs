'''Print all pairs of anagrams in a given array of strings'''
def pair_of_anagram():
    arr = ["abc","geeksquiz", "geeksforgeeks","abcd", "forgeeksgeeks", "zuiqkeegs"] 
    n = len(arr)    #[['geeksquiz', 'zuiqkeegs'], ['geeksforgeeks', 'forgeeksgeeks']]
    ans = []

    i = 0
    j = 1
    # print(sorted(arr[i]))
    for i in range(n):
        for j in range(i+1,n):
            if sorted(arr[i]) == sorted(arr[j]):
                ans.append([arr[i],arr[j]])

    print(ans)

# pair_of_anagram()

'''Longest Common Prefix'''
def longest_prefix():
    strs = ["flower", "flow", "flight"] #fl

    n = min(strs, key = len)
    n = len(n)
    # print(n)
    res = ''
    flag = True
    for i in range(n):
        t = strs[0][i]
        for item in strs:
            if item[i] != t:
                # print(t)
                flag = False
                break
        if flag:
            res += t
        else:
            break

    print(res) 

# longest_prefix()


'''Valid Parentheses '''
def valid_parenthesis():
    t = "[([])]"
    t = '[()]{}{[()()]()}'
    a = []
    x = '()'
    y = '[]'
    z = '{}'
    for i in t:
        if i in '([{':
            a.append(i)
        elif i in ')]}':
            t = a[-1] + i
            if t == x or t == y or t==z:
                a.pop(-1)
                
    print(len(a) == 0)

# valid_parenthesis()

'''Check if Palindrome Ignoring Punctuation'''
def palindrome_ignore_punc():
    t = "A man, a plan, a canal: Panama"    #amanaplanacanalpanama
    t = t.lower()
    t2 = str()
    for i in t:
        if i in 'abcdefghijklmnopqrstuvwxyz':
            t2 += i
    print(t2)
    print(t2 == t2[::-1])

    i = 0
    j = len(t2) - 1
    flag = True
    while i <= j:
        if t2[i] != t2[j]:
            flag = False
            break
        i +=1
        j -=1
    print(flag)

# palindrome_ignore_punc()

'''Encode and Decode Strings'''

def encode_decode_str():
    t = "abbcccddd"     #ab2c3d3
    # t = 'wxyz'
    count = 1
    i = 1
    res = ''
    while i < len(t):
        if t[i] != t[i-1]:
            if count == 1:
                res += t[i-1]
            else:
                res += t[i-1] + str(count)
                count = 1
        elif t[i] == t[i-1]:
            count +=1
        i += 1

    res += t[i-1] + str(count)
    print(res)

    o = 'a1b2c3d3'  #abbcccddd

    j = 0
    k = 1
    ans = ''
    def extnd(s:str,n:int):
        print(s,n)
        ans = ''
        i = 0
        while i < (n):
            ans += s
            i += 1
        return ans
        
    while k < len(o):
        t = extnd(o[j],int(o[k]))
        ans += t
        j += 2
        k +=2
        
    print(ans)

encode_decode_str()