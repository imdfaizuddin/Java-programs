/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public void deleteNode(ListNode node) {
        //assigning next node's value to current node
        node.val= node.next.val;
        //assigning next node's next node adress to current node.next
        node.next= node.next.next;
    }
}
