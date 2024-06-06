'''String to sorted list (sorted(str))'''
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

'''Replace char in string'''
def replace_char():
    s = "hello"
    new = ''
    for i in range(len(s)-1,-1,-1):
        new = new + s[i]
    new = new.replace('l','k')   # okkeh
    print(new)
# replace_char()

'''Using Zip function'''

def zip_to_tuple_and_dict():
    a = ("John", "Charles", "Mike")
    b = ("Jenny", "Christy", "Monica", "king")

    x = zip(a, b)   #The zip function pairs elements from a and b into a zip object. need to convert to tuple to print
                    # The zip function iterates over the shortest input iterable. In this case, both a and b have length 3. Thus, zipping takes O(n) time, where nn is the number of elements in the tuples.
    y = tuple(x)
    print(y)        #(('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica'))
    print(y[0][1])  # Jenny
    print(dict(y))  # {'John': 'Jenny', 'Charles': 'Christy', 'Mike': 'Monica'}

zip_to_tuple_and_dict()