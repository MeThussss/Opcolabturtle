import turtle
import math

class Shape:
    def __init__(self, color):
        self.color = color

    def draw(self):
        pass
    
    #def set_color(self, color):
       #self.color = color

class Flower(Shape):
    def __init__(self, num_petals, radius, color):
        super().__init__(color)
        self.num_petals = num_petals
        self.radius = radius
    
    #def set_num_petals(self, num_petals):
        #self.num_petals = num_petals
        
    #def set_radius(self, radius):
        #self.radius = radius

    def draw(self):
        angle = 360 / self.num_petals
        turtle.color(self.color)  
        for _ in range(self.num_petals):
            turtle.circle(self.radius)
            turtle.left(angle)
        
class CenteredCircle(Flower):
    def __init__(self, num_petals, radius, color, circle_radius, circle_color):
        super().__init__(num_petals, radius, color)
        self.circle_radius = circle_radius
        self.circle_color = circle_color
        
    #def set_circle_radius(self, circle_radius):
        #self.circle_radius = circle_radius
    
    #def set_circle_color(self, circle_color):
        #self.circle_color = circle_color
        
    def draw(self):
        super().draw()
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        turtle.color(self.circle_color)
        turtle.begin_fill()
        turtle.circle(self.circle_radius)
        turtle.end_fill()

# สร้างดอกไม้วงที่1
flower0 = Flower(num_petals=16, radius=125, color="orange")
flower0.draw()

# สร้างดอกไม้วงที่2
flower1 = Flower(num_petals=12, radius=100, color="blue")
flower1.draw()

# สร้างดอกไม้วงที่3
flower2 = Flower(num_petals=8, radius=75, color="red")
flower2.draw()

#สร้างเกสร
centered_circle = CenteredCircle(num_petals=4, radius=50, color="green", circle_radius=20, circle_color="yellow")
centered_circle.draw()

turtle.done()
