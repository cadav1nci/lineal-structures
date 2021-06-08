class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
    
    def add_next(self,next):
        self.next=next
    
    def set_data(self,data):
        self.data=data

    def get_data(self):
        return str(self.data)

    

if __name__=="__main__":
    head = None
    for i in range(1,10):
        head = Node(i,head)
    while head != None:
        print(head.data)
        head = head.next