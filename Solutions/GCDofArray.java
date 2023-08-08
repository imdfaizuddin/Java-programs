/*
Q) Given an integer array nums, return**** the greatest common divisor of the smallest number and largest number in nums.
*/
class Solution {
	public int findGCD(int[] nums) {
		// Your code goes here
        int max=nums[0];
        int min= nums[0];
        for(int i=0;i<nums.length;i++){
            if(nums[i]> max){
                max=nums[i];
            }
            if(nums[i]< min){
                min=nums[i];
            }
        }
        int gcd = 1;
        for(int i=1;i<=max;i++){
            if(max%i==0 && min%i==0){
                gcd = i;
            }
        }
        return gcd;
	}
}
