def frequencyOfElements(nums:list)-> None:
    frequency = {}

    # iterating over the list
    for item in nums:
    # checking the element in dictionary
        if item in frequency:
        # incrementing the counr
            frequency[item] += 1
        else:
        # initializing the count
            frequency[item] = 1

        # printing the frequency
    print(frequency)


def removeDuplicates(nums:list)-> list:
    no_duplicates = list(set(nums))
    return no_duplicates  


l = [1,2,1,2,3,5,5,3,7,7,1,3]

# print(frequencyOfElements(l))
# print(removeDuplicates(l))
# Practice
def noOfElements(nums:list)-> dict:
    freq = {}
    for item in nums:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq

def removeDup(nums:list)-> list:
    ans = list(set(nums))
    return ans
    

print(noOfElements(l))
print(removeDup(l))