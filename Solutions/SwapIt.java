/*
Given two integers, write a function to swap them without using a temporary variable.
*/
class Solution {
	public int[] canSort(int a, int b) {
		
		a=a+b;
		b=a-b;
		a=a-b;
		int sol[]={a,b};
		return sol;
	}
}
