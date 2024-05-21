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

# rotate_str_by_k()

'''Least & most occurring char in a string'''
def least_and_most():
    s = 'GeeksfggorGeeks'
    s = 'Mississippi'   #least occuring char: ' m ' most occuring char:  i
    s = s.lower()

    freq = dict()

    for char in s:
        freq[char] = freq.get(char,0)+1
        min = freq[s[0]]
        max = freq[s[0]]
        val = s[0]
        val2 = s[0]
    for key in freq:
        if freq[key] < min:
            val = key
            min = freq[key]
        if freq[key] > max or (freq[key] == max and val2 > key):
            val2 = key
            max = freq[key]
    print("least occuring char: '",val, "' most occuring char: ", val2)
    print(freq)

# least_and_most()

''' Replace multiple words with K'''

def replace_words_with_k():
    test_str = 'Geeksforgeeks is best for geeks and CS'     #Geeksforgeeks is gfg gfg geeks and gfg
    word_list = ["best", 'CS', 'for']
    repl_wrd = 'gfg'

    arr = test_str.split(" ")

    for item in arr:
        if item in word_list:
            idx = arr.index(item)
            arr[idx] = repl_wrd
        
    print(' '.join(arr))

replace_words_with_k()