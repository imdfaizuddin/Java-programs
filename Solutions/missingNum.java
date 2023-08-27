/*
O(n) solution
*/
class Solution {
	public int findDuplicate(int[] nums) {
		// Your code goes here
        int n=nums.length-1;
        long sum= (n*(n+1))/2;
        long sumArr=0;
        for(int i=0;i<nums.length;i++){
            sumArr+=nums[i];
        }
        long ans=sumArr-sum;
        return (int)ans;
	}
}
