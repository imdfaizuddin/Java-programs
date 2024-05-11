# The ord() function returns the number representing the unicode code of a specified character.
def ord_func():
    print(ord("A")) #output 65
    print(ord("Z")) #output 90
    print(ord("a")) #output 97
    print(ord("z")) #output 122
def print_nextline():
    print("Hello", "end", 87, True, end="\n") #end="\n" == print in nextline
    print("next line")

x = 10
y = 3
print(x//y) #returns the 'integer' or 'floor' value quotient


def string_methods():
    hello = "heLLo World"
    print(hello.upper())    #HELLO WORLD
    print(hello.lower())    #hello world
    print(hello.capitalize())   #Hello world
    print(hello.count("l")) # 1 counts the number of 'l'
    print(hello.lower().count("l")) # 3 converts the string into lowercase then counts the no. of "l"

# and > or > not precedence
print( not(False or False and False))

def take_input():
    name = input("Name: ")
    print(name)

'''for i in range(start, stop, step) start & step are optional'''
'''for i in arr:''' # this iterates over all items in a list
def for_loop(arr, x):
    # n = int(input("n: "))
    import random
    # arrx = [random.randint(0,101),random.randint(0,101),random.randint(0,101),random.randint(0,101),random.randint(0,101),]
    arrx = [37,15,61,77,101]
    if x == 0:
        for i in range(arr[0],arr[1],arr[2]):
            print(i)
    if x == 1:
        for i in arrx:
            print(i)
    if x == 2:
        for i, val in enumerate(arrx):   # i = index , element = values
            print(i, val)

# arr = [0]*3
# arr[0] = int(input("start: "))
# arr[1] = int(input("stop: "))
# arr[2] = int(input("step: "))
# x = int(input("x: "))
# for_loop(arr,x)

def while_loop():
    i = 0
    while True:
        if i == 5:
            i += 1  #else infinite loop because i always == 5
            continue
        print(i)
        i += 1
        if i == 7:
            break

# while_loop()

# Slice operator works on 'string' 'tuple' & 'list'
# sliced = [start:stop:step]
def slice_operator():
    x = [0,1,2,3,4,5,6,7,8,9]
    y = ['hi', 'hello', 'goodbye', 'cya' , 'sure']
    s = "hello"

    sliced = x[0:4:2]   # [0,2]
    print(x[:6])    # [0, 1, 2, 3, 4, 5] start at first index end at 6 index
    print(x[2:])    # [2, 3, 4, 5, 6, 7, 8, 9] start at 2 end at last index
    print(x[2:7])   # [2, 3, 4, 5, 6]   start at 2 end at 7 index
    print(x[::2])   # [0, 2, 4, 6, 8] like for loop iterates 2 steps at a time
    print(x[4:2:-1])    # [4, 3] starts at 4 ends at 2 takes -1 steps
    print(x[::-1])  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] starts at fist ends at last but iterates in opposite direction and reverses the item
    print(s[::-1])  # olleh - starts at fist ends at last but iterates in opposite direction and reverses the item
    print(sliced)

# slice_operator()

'''set is an unordered unique collection of elements'''
'''Looking things up in sets is in constant time much faster than lists'''
def set_datatype():
    x = set()       #for empty set
    s = {4,32,2,2}  #set literal
    s.add(5)
    s.remove(4)
    print(s)
    print(2 in s)   #constant time returns boolean
    print(7 in s)   #constant time returns boolean
    s2 = [4,32,2,2]
    print(2 in s2)  #not in constant time takes much longer comparatively

# set_datatype()

'''lambda function - one line function '''
def lambda_func():
    square = lambda x: x*x
    sum = lambda a,b: a+b
    print(square(5))
    print(sum(2,3))

# lambda_func()

'''Counter'''
def counter_method():
    from collections import Counter
    
    print(Counter(['B','B','A','B','C','A','B','B','A','C']))   #   Counter({'B': 5, 'A': 3, 'C': 2})

    print(Counter({'A':3,'B':5, 'C':2}))    #   Counter({'B': 5, 'A': 3, 'C': 2})

    print(Counter(A=3,B=5,C=2))     #   Counter({'B': 5, 'A': 3, 'C': 2})

    x = dict(Counter([1,2,5,1,3,2,1,6,5,2]))    #   {1: 3, 2: 3, 5: 2, 3: 1, 6: 1}
    print(x)

# counter_method()

def comprehensions_exp():
    x = [x*x for x in range(5)]
    print(x)
    
    y = [[0 for x in range(5)] for x in range(3)]
    print(y)
    
    z = [x for x in range(100) if x%5 == 0]
    print(z)
    
    dic = {i:0 for i in range(100) if i%5 ==0 }
    print(dic)

# comprehensions_exp()

def func_exp(x,y, z = None):
    print('Run',x,y,z)  #   Run 5 6 None(when no z value is passed) # Run 5 6 7 (when z value is passed in func_exp call)
    return x* y, x/y

r1,r2 = func_exp(5,6,7)   # r1 is getting x*y return value, r2 is getting x/y value
print("r1=",r1,"r2=",r2)    #  r1= 30 r2= 0.8333333333333334