# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def recursive_sum(nodes, multiple)->int:
            if nodes == None:
                return 0
            else:
                return nodes.val*multiple + recursive_sum(nodes.next,multiple*10)
        
        l1_sum = recursive_sum(l1,1)
        l2_sum = recursive_sum(l2,1)
        l3_sum = l1_sum + l2_sum

        # convert l3_sum into list of nodes
        l3_string = list(str(l3_sum))
        l3_string.reverse()

        l3_node_head = ListNode(val=int(l3_string[0]),next=None)
        temp_node = l3_node_head

        for i in l3_string[1:]:
            next_node = ListNode(val=int(i),next=None)
            temp_node.next = next_node
            temp_node = next_node
        
        return l3_node_head



                
