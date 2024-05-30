'''Python program to capitalize the first and last character of each word in a string'''
def Capitalize_first_and_last_char():
    s = 'hello world'

    arr = s.split(" ")

    for i in range(len(arr)):
        res = ''
        f = arr[i][0].upper()
        l = arr[i][-1].upper()
        m = arr[i][1:-1]
        arr[i] = f+m+l
        
    ans = " ".join(arr)
    print(ans)

# Capitalize_first_and_last_char()

'''Convert Second Half of the String to Uppercase'''

def uppercase_half_string():
    s = 'apples'

    half = len(s)//2

    j = half

    first = s[:half]
    shalf = s[half:].upper()
    # print(shalf)  #to check second half

    s = first + shalf
    print(s)
    ans = ''
    for i in range(len(s)):
        if i >= half:
            ans = ans + s[i].upper()
        else:
            ans = ans + s[i]

    print(ans)

# uppercase_half_string()

'''Python program to print even length words in a string'''

def even_length_words():
    s = "i am legend alright"

    arr = s.split(" ")
    ans = ''
    for item in arr:
        if len(item)%2 == 0:
            ans = ans + item + " "

    print(ans)

# even_length_words()

'''Python program to check if a string has at least one letter and one number'''
def one_letter_and_number():
    s = 'Hello2'
    flag_1 = False
    flag_2 = False

    for i in s.lower():
        if i in "abcdefghijklmnopqrstuvwxyz":
            flag_1 = True
        if i in "0123456789":
            flag_2 = True

    print(flag_1 and flag_2)


# one_letter_and_number()

'''Python Program to Accept the Strings Which Contains all Vowels'''

def string_all_vovels():
    s1 = "geeksforgeeks"
    s2 = "ABeeIghiObhkUul"

    v = set("aeiou")
    st = set({})

    for char in s2.lower():
        if char in v:
            st.add(char)
        else:
            continue
    
    print(len(v) == len(st))

# string_all_vovels()

'''Count the Number of matching characters in a pair of string'''

def no_of_matching_char():
    str1 = 'abcdef'
    str2 = 'defghia'
    str2 = 'aabcddekll12@'
    str1 = 'bb2211@55k'
    s = set()
    count = 0

    for char in str1:
        if char in s:
            continue
        else:
            if char in str2:
                s.add(char)
                count +=1

    print(count)    # 5

# no_of_matching_char()

'''String Compression IMPORTANT!'''

def string_compress():
    s = 'aabcccc'   #a2b1c4
    s = 'aabcccccaaa'   #a2b1c5a3
    n = len(s)
    i = 1
    count = 1
    res = ''
    while i < n:
        if s[i] == s[i-1]:
            count +=1
        else:
            res = res + s[i-1] + str(count)
            count = 1
        i += 1

    res = res + s[i-1] + str(count)
    print(res)  

# string_compress()

'''Python program to find uncommon words from two Strings'''
def uncommon_words():
    A = "Geeks for Geeks"
    B = "Learning from Geeks for Geeks"     #['Learning', 'from'] {'from', 'Learning'}

    a = A.split()
    b = B.split()
    # print(a,b)

    if len(a)<len(b):
        a,b = b,a
    ans = []
    for i in a:
        if i not in b:
            ans.append(i)
    print(ans)

    print(set(a) - set(b))

uncommon_words()