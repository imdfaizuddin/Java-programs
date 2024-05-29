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

max_frequency()