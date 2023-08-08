/*
Q) Given an array nums of n integers . Find the maximum number from an array.
*/
class Solution {
    public int findLargestElement(int []nums) {
        // Your code goes here
            int max=nums[0];
        for(int i=0;i<nums.length;i++){
            if(nums[i]> max){
                max=nums[i];
            }
    }
    return max;
}
}
