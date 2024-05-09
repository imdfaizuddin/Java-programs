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