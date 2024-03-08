/*
https://www.codingninjas.com/studio/problems/reverse-an-array_8365444?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
 Reverse an Array
Easy
40/40
Average time to solve is 10m
Contributed by
92 upvotes
Asked in company
Problem statement

Given an array 'arr' of size 'n'.


Return an array with all the elements placed in reverse order.


Note:

You don’t need to print anything. Just implement the given function.

Example:

Input: n = 6, arr = [5, 7, 8, 1, 6, 3]

Output: [3, 6, 1, 8, 7, 5]

Explanation: After reversing the array, it looks like this [3, 6, 1, 8, 7, 5].

Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1:

8
3 1 1 7 4 2 6 11

Sample Output 1:

11 6 2 4 7 1 1 3    

Explanation Of Sample Input 1 :

After reversing the array, it looks like this [11, 6, 2, 4, 7, 1, 1, 3].

Sample Input 2:

4
8 1 3 2

Sample Output 2:

2 3 1 8

Explanation Of Sample Input 2 :

After reversing the array, it looks like this [2, 3, 1, 8].

Expected time complexity

The expected time complexity is O(n).

Constraints:

1 <= 'n' <= 10^6
-10^9 <= 'arr[i]' <=10^9


*/

public class Solution {
    public static int[] recur(int i , int j, int[] arr){
        if(i<=j){
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
        recur(++i, --j, arr);
        }
        return arr;
        
    }
    public static int[] reverseArray(int n, int []nums) {
        // Write your code here.
        int i = 0;
        int j = n-1;
        return recur(i, j, nums);
        
    }
}
