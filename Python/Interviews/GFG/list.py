'''Swap elements in String list'''
def swap_elements_in_string_list():
    # Initializing list
    test_list = ['Gfg', 'is', 'best', 'for', 'Geeks']

    for item in test_list:
        # print(item)
        index = test_list.index(item)
        test_list[index] = item.replace('G','_').replace('e','E')
        # print(item)

    print(str(test_list))

# print(swap_elements_in_string_list())

'''Remove empty List from List'''
def remove_empty_list():
    test_list = [5, 6, [], 3, [], [], 9]

    ans = [i for i in test_list if i != []] # [5, 6, 3, 9]

    print(ans)
    #modify the original list
    while [] in test_list:
        test_list.remove([])
        
    print(test_list)    # [5, 6, 3, 9]

# remove_empty_list()

'''Convert List to List of dictionaries'''
def list_of_list_to_dict():
    test_list = ['Gfg', 3, 'is', 8]
    key_list = ['name', 'id']

    # [{‘name’: ‘Gfg’, ‘id’: 3}, {‘name’: ‘is’, ‘id’: 8}] 

    ans = []

    i = 0
    j = 1
    # print(test_list,key_list)
    while j < len(test_list):
        f = {}
        f[key_list[0]] = test_list[i]
        f[key_list[1]] = test_list[j]
        ans.append(f)
        i+=2
        j+=2
        
    print(ans)  # [{'name': 'Gfg', 'id': 3}, {'name': 'is', 'id': 8}]

# list_of_list_to_dict()

'''Split String of list on K character'''
def split_on_k():
    test_list =['Gfg is best', 'for Geeks', 'Preparing']
    # ['Gfg', 'is', 'best', 'for', 'Geeks', 'Preparing']
    res = []
    k = " "
    for item in test_list:
        s = item.split(k)
        res.extend(s)

    print(res)
    '''Using String methods .join() and .split()'''
    s = test_list
    res = ' '.join(s)
    print(res.split(k))

split_on_k()

'''Program to print duplicates from a list of integers'''

def duplicates_in_list():
    list1 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]   # [20, 30, 60, -20]   or {20, -20, 30, 60}

    dup = []
    uni = []

    for i in list1:
        if i not in uni:
            uni.append(i)
        elif i not in dup:
            dup.append(i)
            

    print(dup)
    #or
    x = filter(lambda x: list1.count(x)>1,list1)
    print(set(x))

duplicates_in_list()

'''Sum of number digits in List'''
t = [12, 67, 98, 34]

def sum_of_digits(t):
    a = []
    for item in t:
        s = str(item)
        sum1 = 0
        for i in s:
            sum1 += int(i)
        a.append(sum1)
    return a
    
print(sum_of_digits(t)) #[3, 13, 17, 7]