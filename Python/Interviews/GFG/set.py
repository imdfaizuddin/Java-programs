'''Check if two lists have at-least one element common'''

def common_in_two_lists():
    a = [1, 2, 3, 4, 5]
    b = [5, 6, 7, 8, 9]

    common = set(set(a) & set(b))
    print(common)

    for i in a:
        if i in b:
            print(i, "is common")
# common_in_two_lists()

'''Find missing and additional values in two lists'''
def missing_additional_vals():
    list1 = [1, 2, 3, 4, 5, 6]
    list2 = [4, 5, 6, 7, 8]

    additional_val = set(list1) - set(list2)
    missing_val = set(list2) - set(list1)
    print(additional_val , missing_val)
missing_additional_vals()