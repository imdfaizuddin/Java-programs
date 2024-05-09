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