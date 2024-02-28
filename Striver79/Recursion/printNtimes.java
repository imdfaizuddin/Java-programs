/*
https://www.codingninjas.com/studio/problems/-print-n-times_8380707?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
*/
/*
 Problem statement

You are given an integer ‘n’.


Print “Coding Ninjas ” ‘n’ times, without using a loop.


Example:

Input: ‘n’  = 4

Output:
Coding Ninjas Coding Ninjas Coding Ninjas Coding Ninjas 

Explanation: “Coding Ninjas” is printed 4 times. 


Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1:

3


Sample Output 1:

Coding Ninjas Coding Ninjas Coding Ninjas 


Explanation of sample output 1:

“Coding Ninjas” is printed 3 times. 


Sample Input 2:

5


Sample Output 2:

Coding Ninjas Coding Ninjas Coding Ninjas Coding Ninjas Coding Ninjas 


Expected Time Complexity:

Try to solve this in O(n).


Expected Space Complexity:

Try to solve this in O(n).


Constraints:

1 <= 'n' <= 10^4

Time Limit: 1 sec

*/

import java.util.*;
public class Solution {
    static List<String> list = new ArrayList<>();
    public static List<String> printNtimes(int n){
        // Write your code here.
        if(n==0){
            return list;
        }
        list.add("Coding Ninjas");
        printNtimes(n-1);
        return list;
    }
}
