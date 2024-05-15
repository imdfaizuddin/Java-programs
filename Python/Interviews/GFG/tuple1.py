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

extract_tup_having_k_ele()