l = [1,2,9,9,3,7,2,8,3,7]
# l = l[::-1]
def second_largest_ele(nums):
    largest = nums[0]
    second_largest = nums[0]
    
    for item in nums:
        if item > largest:
            second_largest = largest
            largest = item
        if item < largest and item > second_largest:
            second_largest = item
    
    return second_largest
    
print(second_largest_ele(l))
