#WAP to reverse every word of a strng in proper order
# I/P : 'this is my book'
# O/P : 'siht si ym koob'

def reverse_str(line):
    arr = line.split(" ")
    arr = arr[::-1]
    s = " ".join(arr)
    s = s[::-1]
    return s

line = "this is my book"
ans = reverse_str(line)
print(ans)

def rev_str_map(line):
    ar = line.split()
    ar1 = list(map(lambda x: x[::-1],ar))
    print(' '.join(ar1))

rev_str_map(line)

def rev_str_loop(e):
    t1 = ''
    temp = ''
    for i in e:
        if i != ' ':
            temp += i
        else:
            t1 += temp[::-1] + ' '
            temp = ''
    t1 += temp[::-1]
    print(t1)

rev_str_loop(line)