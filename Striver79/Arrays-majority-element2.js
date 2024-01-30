/*
https://leetcode.com/problems/majority-element-ii/
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
*/
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var majorityElement = function(nums) {
    
    let n = nums.length;
    let n3 = Math.floor(n/3);
    let ans = [];
    let map = new Map();
    for(let i=0; i< nums.length ; i++){
        if(map.has(nums[i])){
            let temp = map.get(nums[i]);
            temp++
            map.set(nums[i], temp);
        }else{
            map.set(nums[i], 1);
        }
    }
    map.forEach(function(value, key){
        if( value > n3){
            ans.push(key);
        }
    })
    return ans;
};

// Solution using object 

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var majorityElement = function(nums) {
    const arrayLength = Math.floor(nums.length / 3);
    const obj = {};
    const res = [];

    for (let i = 0; i < nums.length; i++) {
        if (obj[nums[i]]) {
            obj[nums[i]] = obj[nums[i]] + 1;
        } else {
            obj[nums[i]] = 1;
        }
    }


    for (let key in obj) {
        if (obj[key] > arrayLength) {
            res.push(Number(key));
        }
    }

    return res;
    
};
