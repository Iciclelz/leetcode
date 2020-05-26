/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    let n1 = '';
    let n2 = '';
    
    for (; l1 != null; l1 = l1.next)
    {
        n1 = l1.val + n1;
    }
    
    for (; l2 != null; l2 = l2.next)
    {
        n2 = l2.val + n2;
    }
    
    let n3 = BigInt(n1) + BigInt(n2);
    let s = Array.from(n3.toString());

    let result = new ListNode();
    let p = null;
    let t = result;
    
    while (s.length > 0)
    {
        t.val = Number(s.pop());
        t.next = new ListNode();
        p = t;
        t = t.next;
    }
    
    p.next = null;
    
    return result;
};