/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        
        if (l1 == 0 && l2 == 0)
        {
            return 0;
        }
        
        ListNode *prev = 0;
        ListNode *node = new ListNode(0);
        ListNode *head = node;
        
        while (l1 != 0 && l2 != 0)
        {
            if (l1->val < l2->val)
            {
                //
                node->val = l1->val;
                l1 = l1->next;
            }
            else
            {
                node->val = l2->val;
                l2 = l2->next;
            }
            
            node->next = new ListNode(0);
            prev = node;
            node = node->next;
        }
        
        while (l1 != 0)
        {
            node->val = l1->val;
            l1 = l1->next;
            
            node->next = new ListNode(0);
            prev = node;
            node = node->next;
        }
        
        while (l2 != 0)
        {
            node->val = l2->val;
            l2 = l2->next;
            node->next = new ListNode(0);
            prev = node;
            node = node->next;
        }
        
        prev->next = 0;
        delete node;
        return head;
       
    }
};