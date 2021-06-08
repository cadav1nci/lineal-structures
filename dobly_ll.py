class Node(object):
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class Dnode(Node):
    def __init__(self, data,prev=None, next=None):
        Node.__init__(self,data,next)
        self.prev = prev


if __name__=="__main__":
    head = Dnode(1)
    tail = head

    for data in range(0,6):
        tail.next=Dnode(data,tail)
        tail = tail.next
    probe = tail

    while probe !=None:
        print(probe.data)
        probe = probe.prev
