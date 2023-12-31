/* https://www.geeksforgeeks.org/problems/aggressive-cows/0
You are given an array consisting of n integers which denote the position of a stall. You are also given an integer k which denotes the number of aggressive cows. You are given the task of assigning stalls to k cows such that the minimum distance between any two of them is the maximum possible.
The first line of input contains two space-separated integers n and k.
The second line contains n space-separated integers denoting the position of the stalls.

Example 1:

Input:
n=5 
k=3
stalls = [1 2 4 8 9]
Output:
3
Explanation:
The first cow can be placed at stalls[0], 
the second cow can be placed at stalls[2] and 
the third cow can be placed at stalls[3]. 
The minimum distance between cows, in this case, is 3, 
which also is the largest among all possible ways.

Example 2:

Input:
n=5 
k=3
stalls = [10 1 2 7 5]
Output:
4
Explanation:
The first cow can be placed at stalls[0],
the second cow can be placed at stalls[1] and
the third cow can be placed at stalls[4].
The minimum distance between cows, in this case, is 4,
which also is the largest among all possible ways.
*/

almost On2 solution:
/**
 * @param {number} n
 * @param {number} k
 * @param {number[]} stalls
 * @returns {number}
*/
function canWePlace (stalls, dist , cows){
        let count = 1;
        let last = stalls[0];
        for(let curr of stalls){
            if(curr - last >= dist){
                count++;
                last = curr;
            }
            
        }
        if(count >= cows){
                return true;
            }else{
                return false;
            }
    }

class Solution {
    //Function to solve the problem.
    
    solve(n, k, stalls) {
        //your code here
        stalls.sort(function(a,b){return a-b});
        let m= stalls.length;
        let max = stalls[m-1];
        let min = stalls[0];
        for( let i =1 ; i<=(max-min); i++){
            if(canWePlace(stalls, i , k)== true){
                continue;
            }else{
                return i-1;
            }
        }
    }
}

//  Optimized solution
function canWePlace (stalls, dist , cows){
        let count = 1;
        let last = stalls[0];
        for(let curr of stalls){
            if(curr - last >= dist){
                count++;
                last = curr;
            }
            
        }
        
        if(count >= cows){
                return true;
            }else{
                return false;
            }
    }

class Solution {
    //Function to solve the problem.
    
    solve(n, k, stalls) {
        //your code here
        stalls.sort(function(a,b){return a-b});
        let m= stalls.length;
        let max = stalls[m-1];
        let min = stalls[0];
        // for( let i =1 ; i<=(max-min); i++){
        //     if(canWePlace(stalls, i , k)== true){
        //         continue;
        //     }else{
        //         return i-1;
        //     }
        // }
        let ans = 0;
        let low = 1;
        let high = max-min;
        while(low <= high){
            let mid = Math.floor((low+high)/2);
            if(canWePlace(stalls, mid, k)== true){
                ans = mid;
                low = mid+1;
                // continue;
            }else{
                high = mid-1;
            }
        }
        return ans;
    }
} 
