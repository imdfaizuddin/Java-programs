# Creating a dictionary from personal info
def dict_from_info():
    tup = dict(first="hi",second="how",third="are", fourth="you")
    print (tup)

# a = "apple"
# freq = {a: 1, "app": 3,}
# freq[a] = 2


# print(freq)
# print("apple" in freq)
# print(a in freq)

# # square = lambda x : x*x
# # print(square(5))

# # sum = lambda x, y, z : x + y
# # print(sum(2,3,"x"))

# x = 1
# def demoFunc(x):
#     x += 2
#     print(x)
#     def inside():
#         print(x)
#     inside()
# demoFunc(x)
# print(x)

# name = "Faiz"
# print(f"my name is {name}")

'''Sort Python Dictionaries by Key or Value'''

def sort_by_keys():
    myDict = {'ravi': 10, 'rajnish': 9,
        'sanjeev': 15, 'yash': 2, 'suraj': 32}
    # Convert to list & sort
    ar = list(myDict.keys())
    # print(ar)
    ar.sort()
    sorted_dict = dict()
    for item in ar:
        sorted_dict[item] = myDict[item]
        
    print(sorted_dict)

sort_by_keys()