class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class Stack:

    def __init__(self):
        self.head = None
        self.num_elements = 0

    def push(self, value):
        new_node = Node(value)
        # if stack is empty
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head #place the new node at the head (top) of the linked list
            self.head = new_node

        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return

        value = self.head.value # copy data to a local variable
        self.head = self.head.next #move head pointer to point to next node (top is removed by doing so)
        self.num_elements -= 1
        print(value)

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0
obj1 = Stack()
obj1.push(3)
obj1.push(4)
print(obj1.size())
print(obj1.head.value)
obj1.pop()
print(obj1.size())
