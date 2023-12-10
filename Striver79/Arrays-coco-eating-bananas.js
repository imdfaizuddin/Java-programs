/* https://leetcode.com/problems/koko-eating-bananas/description/
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
 

Constraints:

1 <= piles.length <= 104
piles.length <= h <= 109
1 <= piles[i] <= 109
*/
Binary Search solution :-


  /**
 * @param {number[]} piles
 * @param {number} h
 * @return {number}
 */
var minEatingSpeed = function(piles, h) {
    function canEat(k){
        let ans = 0;
        for(item of piles){
            let hr = Math.ceil(item/k);
            ans +=hr;
        }
        if(ans <= h){
            return true;
        }else{
            return false;
        }
    }
    let n = piles.length;
    if(n==1)return Math.ceil(piles[0]/h);
    piles.sort((a,b)=>a-b);
    let low = 1;
    let high = piles[n-1];
    // while(true){
    //     let Eat = canEat(min);
    //     if(Eat){
    //         break;
    //     }else{
    //         min++;
    //         continue;
    //     }
    // }
    while(low <= high){
        let mid = Math.floor((low+high)/2);
        let eat = canEat(mid);
        if(eat){
            min = mid;
            high = mid-1;
            // break;
        }else{
            low = mid+1;
        }
    }
    return min;
};
