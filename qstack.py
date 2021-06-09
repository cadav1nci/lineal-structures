class Queue:
    def __init__(self):
        self.inbound=[]
        self.outbound=[]

    def enqueue(self,data):
        self.inbound.append(data)
    
    def dequeue(self,data):
        if not self.outbound:
            while self.inbound:
                self.outbound.append(self.inbound.pop())
        return self.outbound.pop()
