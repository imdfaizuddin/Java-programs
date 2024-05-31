def max_frequency():
    s1 = "geaeksfaorageaeks"
    s2 = "ABeeIghiObhkUul"
    f = dict()

    for i in s1.lower():
        if i in f:
            f[i] += 1
        else:
            f[i] = 1
    print(min(f))
    print(max(f.values()))
    a = max(f,key=lambda x:f[x])
    print(f,'\n',max(f,key=lambda x:f[x]))
    x = min(filter(lambda x: f[x] == f[a],f))

    y = map(lambda x: f[x]==f[a],f)
    print(list(x),list(y))

# max_frequency()

def string_func():
    s= "This is a random sentence"
    # ['This', 'is', 'a', 'random', 'sentence']
    # ['sentence', 'random', 'a', 'is', 'This']
    # sentence random a is This
    # sihT si a modnar ecnetnes
    # ['sentence', 'random', 'a', 'is', 'This']
    # sentence random a is This
    # ecnetnes modnar a si sihT

    def split_str(s,k):
        res = ''
        a = []
        for i in s:
            if i != k:
                res += i
            else:
                a.append(res)
                res = ''
        a.append(res)
        return a

    def slice_arr(s,start,end,step=1):
        ar = []
        for i in range(start,end,step):
            ar.append(s[i])
        return ar
        
    def join_str(a,k):
        res = ''
        for item in a:
            res += item + k
        return res[:-1]
    def slice_str(s,start,end,step=1):
        ar = ''
        for i in range(start,end,step):
            ar += s[i]
        return ar
    arr = split_str(s," ")
    print(arr)
    sl = slice_arr(arr,len(arr)-1,-1,-1)
    print(sl)
    j = join_str(sl," ")
    print(j)
    print(slice_str(j,len(j)-1,-1,-1))
    ar = s.split()
    print(ar[::-1])
    print(' '.join(ar[::-1]))
    x = ' '.join(ar)
    print(x[::-1])

string_func()