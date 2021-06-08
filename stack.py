from node import Node
import copy

class Stack:
    def __init__(self):
        self.top=None
        self.size=0
    
    def push(self,data):
        node = Node(data)
        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node

        self.size += 1

    def pop(self):
        if self.top:
            data = self.top.data
            self.size -= 1

            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None

            return data
        return "Empty stack, can´t delete anything"
    
    def peek(self):
        if self.top:
            return self.top.data
        else:
            "Empty stack, can´t delete anything"
    
    def clear(self):
        while self.top:
            self.pop()
    #methd to iterate the stack
    def travel(self):
        b = copy.deepcopy(self)
        while b.top:
            print(str(b.top.data)+"\n")
            b.top=b.top.next
        

    def search(self,data):
        b = copy.deepcopy(self)
        while b.top:
            if data == b.top.data:
                print(f'{data} found succesfully')
                break
            b.top=b.top.next
    
    
if __name__ == "__main__":
    a = Stack()

    for i in range(10):
         a.push(i)

    a.travel()

    a.search(2)

    
    
