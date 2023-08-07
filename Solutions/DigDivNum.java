/*
Q) Count the Digits That Divide a Number
*/
class Solution {
	public int countDigits(int num) {
		// Your code goes here
        int count=0;
        int n=num;
        while(num!=0){
            int i=num%10;
            if(n%i==0){
                count++;
            }
            num/=10;
        }
    return count;
	}
}
