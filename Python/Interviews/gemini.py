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

longest_prefix()