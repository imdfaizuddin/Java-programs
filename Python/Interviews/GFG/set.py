'''Check if two lists have at-least one element common'''

def common_in_two_lists():
    a = [1, 2, 3, 4, 5]
    b = [5, 6, 7, 8, 9]

    common = set(set(a) & set(b))
    print(common)

    for i in a:
        if i in b:
            print(i, "is common")
common_in_two_lists()