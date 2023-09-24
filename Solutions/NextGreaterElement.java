/*
Given an array arr[ ] of size N having elements, the task is to find the next greater element for each element of the array in order of their appearance in the array.
Next greater element of an element in the array is the nearest element on the right which is greater than the current element.
If there does not exist next greater of current element, then next greater element for current element is -1. For example, next greater of the last element is always -1.
*/
// Question Link: https://practice.geeksforgeeks.org/problems/next-larger-element-1587115620/0


class Solution
{
    //Function to find the next greater element for each element of the array.
    public static long[] nextLargerElement(long[] arr, int n)
    { 
        // Your code here
        long ans[] = new long[n];
        Stack <Long> stk= new Stack <>();
        for(int i=n-1;i>=0;i--){
            //removing the smaller elements from the stack
            while(!stk.isEmpty() && stk.peek() <= arr[i]){
                stk.pop();
            }
            // returning the next greater element into the answer array
            
            // ckecking if stack is empty 
                if(stk.isEmpty()){
                    ans[i]=-1;
                }else{
                    ans[i]=stk.peek();
                }
            
            //pushing the value into stack
            stk.push(arr[i]);
        }
        return ans;
    } 
}
