/*
Maximum Product Subarray
Given an integer array nums, find a 
subarray
 that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.
Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

Constraints:
1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
*/
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function(nums) {
    let pref =1;
    let suff = 1;
    
    let max = Number.MIN_SAFE_INTEGER;
    let n= nums.length;
    for(let i=0; i<n ; i++){
        if(pref === 0) pref = 1;
        if(suff === 0) suff = 1;
        pref *= nums[i];
        suff *= nums[n-i-1];
        max = Math.max(max,Math.max(pref,suff));
    }
    return max;
};