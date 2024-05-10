list1 = ['silent', 'enlist',"sile", 'inlets', 'tinsel']

str = 'listen'

def check_anag(str, list):
    
    for item in list:
        if sorted(str) == sorted(item):
            print(item, " is anagram")
        else:
            print(item, " is not anagram")

check_anag(str, list1)