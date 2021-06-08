from typing import Sized
from node import Node

class Linked_list:
    def __init__(self):
        self.tail=None
        self.size = 0


    def add(self,data):
        n = Node(data)
        if self.tail == None:
            self.tail = n
        else:
            current = self.tail
            while current.next:
                current = current.next
            current.next = n
        self.size+=1

    def travel(self):
        msg =""
        current = self.tail
        while current:
            msg += current.get_data()+" - "
            current = current.next
        return msg

    def delete(self,data):
        current = self.tail
        prev = self.tail
        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    prev.next = current.next
                    self.size -=1
                    #nodo eliminado
                    current.data
            prev = current
            current = current.next
    
    def search(self,data):
        for node in self.travel():
            if data == node:
                print(f'Node {data} found')

    def clear(self):
        self.tail=None
        self.size=0


 
    def get_size(self):
        return self.size
    
if __name__=="__main__":
    a = Linked_list()

    for i in range(10):
        a.add(i)

    print( a.travel())
    print(a.size)

    a.delete(3)
    print( a.travel())
    print(a.size)

    a.search(4)



                
        