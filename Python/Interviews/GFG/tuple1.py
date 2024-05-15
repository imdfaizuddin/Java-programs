'''Extract tuples having K digit elements'''
def extract_tup_having_k_ele():
    test_list = [(54, 2), (34, 55), (222, 23), (12, 45), (78, ),(11,22,33)]
    k = 2

    # Output : [(34, 55), (12, 45), (78,)] 
    ans = []
    for tup in test_list:
        flag = True
        for item in tup:
            if len(str(item)) != k:
                flag = False
        if flag == True:
            ans.append(tup)
            

    print(ans)

# extract_tup_having_k_ele()

'''Extract Symmetric Tuples'''
def symmetric_tuple():
    t_list = [(6, 7), (2, 3), (7, 5),(6, 5),(5, 7)] # {(7, 5)}
    # print(set(t_list))
    # print(t_list[0] == t_list[2])

    from collections import Counter

    # print(Counter(t_list[0])==Counter(t_list[2]))
    n = len(t_list)
    ans = set()
    for i in range(n):
        for j in range(i+1,n):
            if Counter(t_list[i])==Counter(t_list[j]):
                ans.add(t_list[i])
            
    print(ans)  #{(7, 5)}

symmetric_tuple()  