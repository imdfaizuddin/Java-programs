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

word_position()