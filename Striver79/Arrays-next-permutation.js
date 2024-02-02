/*
https://leetcode.com/problems/next-permutation/description/
3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100
*/

/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var nextPermutation = function(nums) {
    let n = nums.length;
    let idx = -1;
    for(let i = n-2; i>=0 ; i--){
        if(nums[i]< nums[i+1]){
            idx = i; //breakpoint
            break;
        }
    }
    //if breakpoint does not exist
    if(idx == -1){
        return nums.reverse();
    }

    //finding next greater element
    for(let i= n-1 ; i > idx ; i--){
        if (nums[i] > nums[idx]) {
            [nums[i], nums[idx]] = [nums[idx], nums[i]]; // swap A[i] and A[ind]
            break;
        }
    }
    nums.splice(idx + 1, n - idx - 1, ...nums.slice(idx + 1).reverse());

};
