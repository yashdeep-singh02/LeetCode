/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode inter = null;
        int l1=0, l2=0;
        ListNode current1 = headA;
        ListNode current2 = headB;
        while(current1!=null)
        {
            l1++;
            current1=current1.next;
            
        }
          while(current2!=null)
        {
            l2++;
            current2=current2.next;
            
        }
        current1 = headA;
        current2 = headB;
        while(l1>l2)
        {
           current1=current1.next;
           l1--;
        }
          while(l2>l1)
        {
           current2=current2.next;
           l2--;
        }
        while(current1!=null && current2!=null)
        {
            if (current1 == current2)
               return current1;
            
            current1 = current1.next;
            current2 = current2.next;
        }
        return inter;
    }
}