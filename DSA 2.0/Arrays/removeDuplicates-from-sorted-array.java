class Solution {
    public int removeDuplicates(int[] nums) {
        int j = 0;
        int sum = 1;
        for(int i = 1 ; i<nums.length; i++){
            if(nums[j] != nums[i]){
                nums[j+1] = nums[i];
                j++;
                sum++;
            }
        }
        return sum;
    }
}
