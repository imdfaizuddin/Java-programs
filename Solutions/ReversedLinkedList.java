/*
Reverse Linked List o(n)
*/
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        //to reverse a linked list 3 variables
         ListNode prev= null;
        ListNode curr=head;
        ListNode next;
        while(curr != null){
            //4 steps to reverse a linked list
            next=curr.next;
            curr.next=prev;
            prev=curr;
            curr=next;
        }
        head=prev;
        return prev;
    }
}
