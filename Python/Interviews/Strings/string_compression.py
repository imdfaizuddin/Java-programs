def shrtn_str(str):
    n = len(str)
    i = 0
    j = 1
    count = 1
    ans = ""
    while j < n:
        if str[i] == str[j]:
            # print("True")
            count += 1
            j +=1
        else:
            ans = f"{ans}{str[i]}{count}"
            # print(ans)
            count = 1
            i = j
            j += 1
    ans = f"{ans}{str[i]}{count}"
    print(ans)

str = "aabcccccaaag"
shrtn_str(str)