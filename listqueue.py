class ListQueue:
    def __init__(self):
        self.items = []
        self.size = 0

    def enqueue(self,data):
        self.items.insert(0,data)
        self.size += 1

    def dequeue(self,data):
        data = self.items.pop()
        self.size -=1
        return data

    def traverse(self):
        for i in range(self.size):
            print(self.items[i])
    
if __name__=="__main__":
    l = ListQueue()
    for i in range(1,10):
        l.enqueue(i)
    
    l.traverse()
    
    

