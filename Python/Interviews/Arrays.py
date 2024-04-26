def frequencyOfElements(nums:list)-> None:
    print(nums)


def removeDuplicates(nums:list)-> list:
    no_duplicates = list(set(nums))
    return no_duplicates  


l = [1,2,1,2,3,5,5,3,7,7,1,3]

print(frequencyOfElements(l))
print(removeDuplicates(l))

