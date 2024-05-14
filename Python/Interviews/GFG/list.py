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

remove_empty_list()