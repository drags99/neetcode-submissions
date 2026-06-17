class Node:
    def __init__(self, val = None, next_node = None):
        self.val = val
        self.next_node = next_node # should be of type Node, unless it is -1

class LinkedList:
    def __init__(self):
        # no head or tail in the begining
        self.tail = Node() # dummy tail

        # head just points to the tail
        self.head = Node(val = None, next_node = self.tail)
    
    def get(self, index: int) -> int:
        if index == 0:
            if self.head.val == None:
                return -1
            else:
                return self.head.val 
        else:
            # idx = 1
            node = self.head
            for idx in range(index):
                if node.next_node == None:
                    return -1
                else:
                    node = node.next_node
        return node.val

    def insertHead(self, val: int) -> None:
        # if head value is None then assign
        if self.head.val == None:
            self.head.val = val
        else:
            current_head = self.head
            self.head = Node(val, current_head)

    def insertTail(self, val: int) -> None:
        if self.head.val == None:
            self.head.val = val
        elif self.tail.val == None:
            self.tail.val = val
        else:
            new_tail = Node(val,None)
            current_tail = self.tail
            current_tail.next_node = new_tail
            self.tail = new_tail

    def remove(self, index: int) -> bool:
        print("before remove")
        print(self.getValues())

        current_idx = 0
        current_node = self.head

        # find node before the desired node to be removed
        old_node = current_node
        while current_idx < index:
            # if current_node.val == None:
            #     return False
            old_node = current_node
            current_node = current_node.next_node
            if current_node == None:
                print("next node doesn't exist in remove, return False")
                return False
            current_idx += 1

        # handle head case
        if index == 0 and self.head:
            if self.head.val == None:
                return False

            self.head = self.head.next_node
            
            if self.head.next_node == None:
                self.head = Node(None,self.tail)
            return True
        
        # handle tail case
        if current_node.next_node == None:
            if current_node.val == None:
                return False
            print("after")
            self.tail = current_node
            self.tail.next_node = None
            return True

        # handle general case
        print(f"general case")
        node_to_remove = old_node.next_node
        replacement_node = node_to_remove.next_node
        old_node.next_node = replacement_node
        return True

    def getValues(self) -> List[int]:
        values = []
        node = self.head
        if node.val == None:
            return values
        while node.next_node != None:
            values.append(node.val)
            node = node.next_node
        
        if self.tail.val != None:
            values.append(self.tail.val)
        return values
