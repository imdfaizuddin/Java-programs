/*
Q) Given an array of integers . Find the smallest element in the array.
*/
class Solution {
	public int findSmallest(int[] nums) {
		
          int smallest= nums[0];
        for(int i=0;i<nums.length;i++){
            if(nums[i]<smallest){
                smallest=nums[i];
            }
	}
    return smallest;
}
}
