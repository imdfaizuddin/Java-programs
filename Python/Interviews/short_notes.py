def sorted_exp():
    str1 = "Hhello"
    s = sorted(str1)    #   ['H', 'e', 'h', 'l', 'l', 'o']  (H < h)     
    x = ''.join(sorted(s))  
    print(x)    # ehllo
    print(s)    # ehllo
    print(str1.swapcase())  #swap the case Hello -> hELLO

sorted_exp()

'''Split and join'''
def split_and_join(line):
    # write your code here
    a = line.split(";")      #   ['hello', 'how', 'are', 'you', '?']
    print(a)
    b = "-".join(a)      # hello-how-are-you-?
    return b

# line = "hello; how; are; you; ?"
# print(split_and_join(line))