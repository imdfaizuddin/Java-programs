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
    d = {}
    for item in nums:
        if item in d:
            d[item] += 1
        else:
            d[item] = 1
    return d

def removeDup(nums:list)-> list:
    ans = []
    for item in nums:
        if item in ans:
            continue
        else:
            ans.append(item)
        
    return ans
    
    

# print(noOfElements(l))
# print(removeDup(l))
# print(removeDuplicates(l))

arr = [0,1,2,3,4,5]

arr.append('hi')    #   [0, 1, 2, 3, 4, 5, 'hi']

arr.remove(2) # [0, 1, 3, 4, 5, 'hi']

arr.pop(2)  # [0, 1, 4, 5, 'hi']
 
arr.insert(2,'hi')  # [0, 1, 'hi', 4, 5, 'hi']

arr[0] = "first index"  #   ['first index', 1, 'hi', 4, 5, 'hi']

'''Remove Duplicate in place in sorted list'''

def rem_dup():
    l = [1,2,1,2,3,5,5,3,7,7,1,3]   # [1, 2, 3, 5, 7] {1, 2, 3, 5, 7}
    n = len(l)
    i = 0
    j = 1
    l.sort()    #[1, 1, 1, 2, 2, 3, 3, 3, 5, 5, 7, 7]

    while j < n:
        if l[j] != l[i]:
            i += 1
            l[i] = l[j]
        j += 1
    l = l[:i+1]
    print(l, set(l))

'''Remove Duplicate in place'''
rem_dup()

def remove_dup(arr):
  i = 0
  j = 1
  while j < len(arr):
    if arr[j] not in arr[:i+1]:
      arr[i+1] = arr[j]
      i += 1
    j += 1
  arr = arr[:i+1]
  return arr
print('ans',remove_dup(l))  #ans [1, 2, 3, 5, 7]