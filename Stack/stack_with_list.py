class Stack:
    def __init__(self):
        self.item = []
        self.num_item = 0
        
         #Initialize the Stack
            
    
    def size(self):
        if self.num_item == 0:
            return self.num_item
        else:
            print(self.num_item)
         #Check the size of the Stack
    
    def push(self, item1):
        if len(self.item)==0:
            self.item = item1
        else:
            self.item.append(item1)
         #Push item onto Stack

    def pop(self):
        if len(self.item)==0:
            return None
        else:
            self.item.pop()
         #Pop item off of the Stack
         
MyStack = Stack()

MyStack.push("Web Page 1")
MyStack.push("Web Page 2")
MyStack.push("Web Page 3")

print (MyStack.item)
