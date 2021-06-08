from a import Array

class Grid:
    def __init__(self,rows,columns,fill_value=None):
        self.data= Array(rows)
        for i in range (rows):
            self.data[i] = Array(columns)
        self.fillup()
    
    def fillup(self):
        for row in range(self.get_height()):
            for column in range(self.get_width()):
                self.data[row][column] = "*"

    def get_height(self):
        return len(self.data)

    def get_width(self):
        return len(self.data[0])
    
    def __getitem__(self,index):
        return self.data[index]
    
    def _str_(self):
        result = ""

        for row in range(self.get_height()):
            for column in range(self.get_width()):
                result += str(self.data[row][column])+" "
            
            result+="\n"

        return str(result)

if __name__=="__main__":
    a = Grid(6,6)
    print(a._str_())
