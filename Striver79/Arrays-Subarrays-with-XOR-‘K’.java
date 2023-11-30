/*
Q) https://www.codingninjas.com/studio/problems/subarrays-with-xor-k_6826258
*/

O(n2) solution:-
  public class Solution {
    public static int subarraysWithSumK(int []a, int b) {
        // Write your code here
        long count = 0;
        for(int i = 0; i<a.length; i++){
            int xor=0;
            for( long j =i ; j<a.length; j++ ){
                xor = xor^a[(int)j];
                if( xor == b) count++;
            }
        }
        return (int)count;
    }
}
