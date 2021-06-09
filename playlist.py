
import time
class Playlist:
    def __init__(self):
        self.items = []
        self.size = 0

    def enqueue(self,song,artist):
        a = [song, artist]
        self.items.append(a)
        self.size += 1

    def dequeue(self,data):
        data = self.items.pop()
        self.size -=1
        return data

    def playAll(self):
        for i in range(self.size):
            print(f'song: {self.items[i][0]} ,artist: {self.items[i][1]}')
            time.sleep(1)
    
if __name__=="__main__":
    p = Playlist()

    
    p.enqueue("acid love","cadavinci")
    p.enqueue("mdma beat","cadavinci")
    p.enqueue("harina","cadavinci")

    p.playAll()
    
    

