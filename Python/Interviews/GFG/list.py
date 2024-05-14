'''Swap elements in String list'''
def swap_elements_in_string_list():
    # Initializing list
    test_list = ['Gfg', 'is', 'best', 'for', 'Geeks']

    # printing original lists
    print("The original list is : " + str(test_list))

    for item in test_list:
        # print(item)
        index = test_list.index(item)
        test_list[index] = item.replace('G','_').replace('e','E')
        # print(item)

    print(str(test_list))

print(swap_elements_in_string_list())