/*
Q) Given an integer number n, return the difference between the product of its digits and the sum of its digits.
*/
class Solution {
	public int subtractProductAndSum(int n) {
		// Your code goes here
        int prod=1;
        int sum=0;
        while(n!=0){
            int i=n%10;
            sum+=i;
            prod*=i;
            n/=10;

        }
        return prod-sum;
	}
}
