import turtle
import math

class Shape:
    def __init__(self, color):
        self.color = color

    def draw(self):
        pass

#การสร้างดอกไม้    
class Flower(Shape):
    def __init__(self, num_petals, radius, color): #กำหนดจำนวนกลีบและขนาดของดอกไม้ รวมถึงสี
        super().__init__(color)
        self.num_petals = num_petals
        self.radius = radius

    def draw(self): #วาดกลีบดอกไม้
        angle = 360 / self.num_petals
        turtle.color(self.color)  
        for _ in range(self.num_petals):
            turtle.circle(self.radius)
            turtle.left(angle)
 
#การสร้างเกสรของดอกไม้โดยมีการสืบทอดการสร้างกลีบของเกสรมาจาก class flower       
class CenteredCircle(Flower):
    def __init__(self, num_petals, radius, color, circle_radius, circle_color): #การกำหนดกลีบรอบ ๆ ของเกสรดอกไม้ และขนาดของเกสรรวมถึงสีที่ต้องการ    
        super().__init__(num_petals, radius, color)
        self.circle_radius = circle_radius
        self.circle_color = circle_color
        
    def draw(self): #วาดเกสรดอกไม้ 
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

#สร้างเกสรชั้นนอก
centered_circle = CenteredCircle(num_petals=4, radius=50, color="green", circle_radius=20, circle_color="yellow")
centered_circle.draw()

#สร้างเกสรชั้นใน
centered_circle = CenteredCircle(num_petals=2, radius=25, color="purple", circle_radius=10, circle_color="white")
centered_circle.draw()

turtle.done()
