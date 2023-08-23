/*
Koko eats banana
https://leetcode.com/problems/koko-eating-bananas/
*/
class Solution {
    int maxElement(int[] arr){
        int max=Integer.MIN_VALUE;
        for(int i: arr){
            if(i>max)max=i;
        }
        return max;
    }

    int totTime(int[] arr, int k){
        int ans=0;
        for(int i: arr){
            ans+=Math.ceil((double)i/(double)k);
        }
        return ans;
    }

    public int minEatingSpeed(int[] piles, int h) {
        int l=1;
        int e= maxElement(piles);
        while(l<=e){
            int mid= l+(e-l)/2;
            int k=totTime(piles,mid);
            if(k>h){
                l=mid+1;
            }else{
                e=mid-1;
            }
        }
        return l;
    }
}
