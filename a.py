class Array:
    def __init__(self,size,):
        i = 0
        self.items = list()
        # fill up the list with a default value
        for i in range(size):
            self.items.append(i)
            i = i+1

    def __len__(self):
        return len(self.items)

    def __str__(self) :
        return str(self.items)
        
    def __iter__(self):
        return iter(self.items)
    
    def __getitem__(self,index):
        return self.items[index]

    def __setitem__(self,index,el):
        self.items[index] = el
    
    def __sum__(self):
        totl = 0
        for i in range(self.__len__()):
            totl = totl + self.items[i]
        return totl

if __name__ == "__main__":
        a = Array(10)

        print(a.__sum__())
        print(a.__len__())
        print(a.__str__())