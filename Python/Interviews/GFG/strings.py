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

uppercase_half_string()