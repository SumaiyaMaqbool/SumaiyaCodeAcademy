class Rectangle:
    def __init__(self, width,hight,col):
        self.width = width
        self.hight = hight
        self.col = col
    def area (self, width, hight):
        area = (self.width*self.hight)
        print("Area is : ", area)
    def perameter (self, width, hight):
        perameter = (self.width)*2 + (self.hight)*2
        print("Perameter is : ", perameter)
    def color (self,col):
        print("Color of the rectangle is : "+ self.col)
        
colour = "Yellow"        
rec=Rectangle(2,5,colour)
rec.area(2,5)
rec.perameter(2,5)
print(rec.col(colour))