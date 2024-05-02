def setExp(my_set:set)-> None:
    for item in my_set:
        print(item)
    
s = {1,3,2,5,"hi",7,1}
s2 = {8,9,5}
setExp(s)
print(list(s | s2)) # | union of two sets
print(list(s & s2)) # & returns common in both sets
print(list(s - s2)) #First set(s) - (s2) (common elements are removed from first set)
print(list(s ^ s2)) # XOR removes common elements in both sets
# x = int(input())
# print(type(x))