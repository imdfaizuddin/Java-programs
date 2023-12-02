/*
Given an array of integers. Find the Inversion Count in the array. 

Inversion Count: For an array, inversion count indicates how far (or close) the array is from being sorted. If the array is already sorted then the inversion count is 0.
If an array is sorted in the reverse order then the inversion count is the maximum. 
Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.
 

Example 1:

Input: N = 5, arr[] = {2, 4, 1, 3, 5}
Output: 3
Explanation: The sequence 2, 4, 1, 3, 5 
has three inversions (2, 1), (4, 1), (4, 3).

Example 2:

Input: N = 5
arr[] = {2, 3, 4, 5, 6}
Output: 0
Explanation: As the sequence is already 
sorted so there is no inversion count.
*/

O(n2) solution:-
class Solution {
    // Function to count inversions in the array.
    inversionCount(arr, N)
    {
        //your code here
        let count = 0;
        for(let i=0; i<N ; i++){
            for(let j=i+1 ; j<N; j++){
                if(arr[i] > arr[j])count++;
            }
        }
      return count;  
    }
}
