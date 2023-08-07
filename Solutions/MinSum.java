/*
Q) Minimum Sum of Four Digit Number After Splitting Digits
*/
class Solution {
	public int minimumSum(int num) {
		// Your code goes here
        int arr[] = new int[4];
        int count=0;
        while(num!=0){
            int i=num%10;
            arr[count]=i;
            num/=10;
            count++;
            }
            Arrays.sort(arr);
            int a= arr[0]*10+arr[2];
            int b= arr[1]*10+arr[3];
            return a+b;
            }
        }
