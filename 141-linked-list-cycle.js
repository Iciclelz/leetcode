/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function(head) {
    
    if (head == null)
    {
        return false;
    }
    
    let tortoise = head;
    let hare = head;
    
    while (hare.next != null && hare.next.next != null)
    {
        tortoise = tortoise.next;
        hare = hare.next.next;
        
        if (hare == tortoise)
		{
			/*
            tortoise = head;
			
            while (tortoise != hare)
			{
				tortoise = tortoise.next;
				hare = hare.next;
			}
            */
			return true;
		}
    }
    
    return false;
};