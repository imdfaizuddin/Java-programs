/*
Two Sum O(n^2)
*/
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int ans[] = new int[2];
        int k=0;
        for(int i=0;i<nums.length;i++){
            for(int j=i+1;j<nums.length;j++){
                int s=nums[i]+nums[j];
                if(s==target){
                    ans[k]=i;
                    ans[k+1]=j;
                }
            }
        }
        return ans;
    }
}
