/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
        
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        
        ListNode dummy = new ListNode(0);
        ListNode cur = dummy;
        
        int carry = 0;
        while (l1 != null && l2 != null){
            int sum = l1.val + l2.val + carry;
            int num = sum % 10;
            carry = sum / 10;
            ListNode tmp = new ListNode(num);
            cur.next = tmp;
            
            cur = cur.next;
            l1 = l1.next;
            l2 = l2.next;
        }
        
        
        if(l1 != null){
            if(carry != 0){
                while (l1 != null){
                    int sum = l1.val + carry;
                    int num = sum % 10;
                    carry = sum / 10;
                    ListNode tmp = new ListNode(num);
                    cur.next = tmp;
                    
                    cur = cur.next;
                    l1 = l1.next;
                }
            }else{
                cur.next = l1;
            }
        }else if (l2 != null){
            if(carry != 0){
                while (l2 != null){
                    int sum = l2.val + carry;
                    int num = sum % 10;
                    carry = sum / 10;
                    ListNode tmp = new ListNode(num);
                    cur.next = tmp;
                    cur = cur.next;
                    l2 = l2.next;
                }
            }else{
                cur.next = l2;
            }
        }
                    
        if (carry != 0){
            ListNode tmp = new ListNode(carry);
            cur.next = tmp;
        }
    
        return dummy.next;
    }
}




/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
        
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        
        ListNode dummy = new ListNode(0);
        ListNode cur = dummy;
        dummy.next = l1;
        
        int carry = 0;
        while (l1 != null && l2 != null){
            int sum = l1.val + l2.val + carry;
            int num = sum % 10;
            carry = sum / 10;
            l1.val = num;
            cur = cur.next;
            l1 = l1.next;
            l2 = l2.next;
        }
        
        
        if(l1 != null){
            if(carry != 0){
                while (l1 != null){
                    int sum = l1.val + carry;
                    int num = sum % 10;
                    carry = sum / 10;
                    cur = cur.next;
                    l1.val = num;
                    l1 = l1.next;
                }
            }
                
        }else if (l2 != null){
            cur.next = l2;
            if(carry != 0){
                while (l2 != null){
                    int sum = l2.val + carry;
                    int num = sum % 10;
                    carry = sum / 10;
                    cur = cur.next;
                    l2.val = num;
                    l2 = l2.next;
                }
            }
        }
        
        if (carry != 0){
            ListNode tmp = new ListNode(carry);
            cur.next = tmp;
        }
                
        return dummy.next;
    }
}