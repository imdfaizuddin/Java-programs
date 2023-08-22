/*
Capacity To Ship Packages Within D Days
*/



class Solution {
    int Numdays(int capacity, int[] weights){
        int day=1;
        int n=weights.length;
        int load=0;
        for(int i=0;i<n;i++){
            if(load+ weights[i] <= capacity){
                load+=weights[i];
            }else{
                day++;
                load=0;
                load= weights[i];
                
            }
        }
        
        return day;
    }
	public int shipWithinDays(int[] weights, int days) {
		// Your code goes here
        int min_capacity=Integer.MIN_VALUE;
        int max_capacity=0;
        int n=weights.length;
        for(int i=0;i<n;i++){
            if(weights[i]>min_capacity){
                min_capacity=weights[i];
            }
            max_capacity+=weights[i];
        }
        
        int s=min_capacity;
        int e=max_capacity;
        int ans=0;
        while(s<=e){
            int mid= s +(e-s)/2;
            int d= Numdays(mid,weights);
            if(d>days){
                s=mid+1;
            }else{
                ans=mid;
                e= mid-1;
            }
        }
        return ans;
	}
}
