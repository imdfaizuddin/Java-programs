str1 = "Hello"
x = ''.join(sorted(str1))   
print(x)    # ehllo

print(str1.swapcase())  #swap the case Hello -> hELLO

'''Split and join'''
def split_and_join(line):
    # write your code here
    a = line.split(" ")      #   ['hello', 'how', 'are', 'you', '?']
    b = "-".join(a)      # hello-how-are-you-?
    return b

line = "hello how are you ?"
print(split_and_join(line))