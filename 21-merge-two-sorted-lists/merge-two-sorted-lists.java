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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {

        ListNode current1 = list1;
        ListNode current2 = list2;
        ListNode dummy = new ListNode(0);
        ListNode current3 = dummy;
        while (current1 != null && current2 != null) {
            if (current1.val < current2.val) {
                current3.next = current1;
                current1 = current1.next;

            } else {
                current3.next = current2;
                current2 = current2.next;

            }
            current3 = current3.next;
        }
        if (current1 == null && current2 != null) {
            while (current2 != null) {
                current3.next = current2;
                current2 = current2.next;
                current3 = current3.next;

            }
        }
        if (current2 == null && current1 != null) {
            while (current1 != null) {
                current3.next = current1;
                current1 = current1.next;
                current3 = current3.next;

            }
        }

        return dummy.next;

    }
}