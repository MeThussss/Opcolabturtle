from ColabTurtlePlus.Turtle import *
import threading
import time

turtle = Turtle()

class Shape:
    def __init__(self, color):
        self.color = color

    def draw(self):
        pass

#การสร้างดอกไม้ 
class Flower(Shape):
    def __init__(self, num_petals, radius, color, x, y):#กำหนดจำนวนกลีบ ขนาดของดอกไม้ รวมถึงสี และตำแหน่งที่ต้องการจะวาด 
        super().__init__(color)
        self.num_petals = num_petals
        self.radius = radius
        self.x = x
        self.y = y

    def draw(self): #วาดกลีบดอกไม้
        angle = 360 / self.num_petals
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color(self.color)  
        for _ in range(self.num_petals):
            turtle.circle(self.radius)
            turtle.left(angle)

#การสร้างเกสรของดอกไม้โดยมีการสืบทอดการสร้างกลีบของเกสรมาจาก class flower       
class CenteredCircle(Flower):
    def __init__(self, num_petals, radius, color, circle_radius, circle_color, x, y): #การกำหนดกลีบรอบ ๆ ของเกสรดอกไม้ ,ขนาดของเกสร รวมถึงสีที่ต้องการ และตำแหน่ง   
        super().__init__(num_petals, radius, color, x , y)
        self.circle_radius = circle_radius
        self.circle_color = circle_color
        
    def draw(self): #วาดเกสรดอกไม้ 
        super().draw()
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color(self.circle_color)
        turtle.begin_fill()
        turtle.circle(self.circle_radius)
        turtle.end_fill()

def draw_flower(flower):#สร้างตัวเรียกฟังก์ชันวาดกลีบดอกไม้เพื่อเรียกใช้งานใน thread
    flower.draw()

def draw_centeredcircle(centeredcircle):#สร้างตัวเรียกฟังก์ชันวาดเกสรดอกไม้เพื่อเรียกใช้งานใน thread
    centeredcircle.draw()

if __name__ == "__main__":
    tic = time.perf_counter()

    turtle.delay(0)  # เพื่อวาดทันทีที่เรียก
    turtle.speed(0)  # ให้วาดดอกไม้ไวมาก

    # สร้างดอกไม้และเกสรในแต่ละตำแหน่ง
    flower1 = Flower(num_petals=16, radius=100, color="orange", x=-200, y = -100)
    flower2 = Flower(num_petals=12, radius=80, color="blue", x=200, y = 100)
    center1 = CenteredCircle(num_petals=4, radius=50, color="green", circle_radius=20, circle_color="yellow", x=-200, y=-100)
    center2 = CenteredCircle(num_petals=3, radius=40, color="red", circle_radius=10, circle_color="purple" ,x=200, y = 100)

    # สร้าง thread สำหรับการวาดดอกไม้ และเกสร
    thread1 = threading.Thread(target=draw_flower, args=(flower1,))
    thread2 = threading.Thread(target=draw_flower, args=(flower2,))
    thread3 = threading.Thread(target=draw_centeredcircle, args=(center1,))
    thread4 = threading.Thread(target=draw_centeredcircle, args=(center2,))

    # เริ่มการทำงานของ thread
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()

    # รอ thread ทำงานเสร็จสิ้น
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()

    print("Done!") #บ่งบอกถึง thread ทั้งหมดเสร็จสิ้นการทำงาน
    toc = time.perf_counter() 
    print(f"Total time: {toc - tic:0.4f} seconds") #แสดงเวลาที่ใช้ในการทำงาน
