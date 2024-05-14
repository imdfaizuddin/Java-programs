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

list_of_list_to_dict()