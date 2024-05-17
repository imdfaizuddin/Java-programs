def word_to_num():
    s1 = 'zero four zero one'
    s2 = "four zero one four"
    num = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    ar = s2.split(" ")
    ans = ''
    for item in ar:
        ans = ans + str(num.get(item))
        
    print(ans)


# word_to_num()

def word_position():
    s1 = 'geeksforgeeks is best for geeks'
    f = "is"
    arr = s1.split(" ")
    ans = 0
    for item in arr:
        if item == f:
            ans = arr.index(item)
            
    print(ans+1)

# word_position()

'''Consecutive characters frequency'''

def consecutive_char_freq():
    text = 'geekksforgggeeks'   # output- [1, 2, 2, 1, 1, 1, 1, 3, 2, 1, 1]
    n = len(text)
    ans = [0]*n
    ar = []
    val = text[0]
    count = 1
    i = 1
    j = 0
    while i < n:
        if text[i] == text[i-1]:
            count += 1
        else:
            ar.append(count)
            ans[j] = count
            j += 1
            count = 1
        i += 1
    ans[j] = count
    ar.append(count)
    print(ans,ar)   # [1, 2, 2, 1, 1, 1, 1, 3, 2, 1, 1, 0, 0, 0, 0, 0] [1, 2, 2, 1, 1, 1, 1, 3, 2, 1, 1]

# consecutive_char_freq()

'''String slicing in Python to Rotate a String'''

def rotate_str_by_k():
    s = "qwertyu"
    # Left rotation : "ertyuqw"
    # Right rotation : "yuqwert"
    s = "GeeksforGeeks"
    # Left Rotation  : "eksforGeeksGe" 
    # Right Rotation : "ksGeeksforGee"  

    d = 2

    def rotate_left(s,d):
        n = len(s)
        res = [0]*n
        for i in range(len(s)):
            res[(i-d)%n] = s[i]
            
        return ''.join(res)
        
    def rotate_right(s,d):
        n = len(s)
        res = [0]*n
        for i in range(len(s)):
            res[(i+d)%n] = s[i]
            
        return ''.join(res)
        
    print(rotate_left(s,d))
    print(rotate_right(s,d))

rotate_str_by_k()