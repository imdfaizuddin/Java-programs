def count_substring(string, sub_string):
    nn = len(sub_string)
    m = len(string)
    n = m-nn
    i = 0
    count = 0
    while i <= n:
        str = "".join(string[i:i+nn])
        # print(str)
        if str == sub_string:
            count += 1
            
        i += 1
    return count
    
string = "ABCDCDCCDCCDCDCDCD"
sub_string = "CDC"

x = count_substring(string,sub_string)
print(x)

def cnt_sub(string,sub_string):

    n = len(string) - len(sub_string)
    nn = len(sub_string)
    count = 0
    for i in range(n):
        if string[i:i+nn] == sub_string:
            count +=1
            
    return count

print(cnt_sub(string,sub_string))