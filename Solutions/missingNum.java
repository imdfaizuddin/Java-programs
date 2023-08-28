/*
O(n) solution
*/
class Solution {
	public int findDuplicate(int[] nums) {
		// Your code goes here
        int n=nums.length-1;
        int sum= (n*(n+1))/2;
        int sumArr=0;
        for(int i=0;i<nums.length;i++){
            sumArr+=nums[i];
        }
        int ans=sumArr-sum;
        return (int)ans;
	}
}
