import turtle

# إحداثيات الوش (Head) مضبوطة
head = [
    (-20, 230),(-80, 220),(-140, 180),(-185, 120),(-210, 40),(-215, -40),(-195, -120),(-155, -180),
    (-100, -220),(-40, -245),(0, -250),(40, -245),(100, -220),(155, -180),(195, -120),(215, -40),
    (210, 40),(185, 120),(140, 180),(80, 220),(20, 230),(0, 235)
]

# العين الشمال
left_eye = [
    (-175, 85),(-145, 115),(-105, 130),(-70, 120),
    (-90, 80),(-125, 50),(-160, 45),(-175, 85)
]

# العين اليمين (معدلة لتكون معكوسة بالموجب)
right_eye = [
    (175, 85),(145, 115),(105, 130),(70, 120),
    (90, 80),(125, 50),(160, 45),(175, 85)
]

web_lines = [    
    [(0, 235), (0, -245)],
    [(0, 190), (-80, 220)],[(0, 140), (-140, 180)],[(0, 80), (-185, 120)],[(0, 20), (-210, 40)],
    [(0, -40), (-215, -40)],[(0, -100), (-195, -120)],[(0, -160), (-155, -180)],[(0, -210), (-100, -220)],
    [(0, 190), (80, 220)],[(0, 140), (140, 180)],[(0, 80), (185, 120)],[(0, 20), (210, 40)],[(0, -40), (215, -40)],
    [(0, -100), (195, -120)],[(0, -160), (155, -180)],[(0, -210), (100, -220)]
]

web_rings = [
    [(-65, 205),(-30, 195),(0, 190),(30, 195),(65, 205)],
    [(-120, 165),(-70, 150),(0, 145),(70, 150),(120, 165)],
    [(-165, 115),(-100, 100),(0, 95),(100, 100),(165, 115)],
    [(-195, 55),(-120, 45),(0, 40),(120, 45),(195, 55)],
    [(-205, -10),(-130, -15),(0, -20),(130, -15),(205, -10)],
    [(-200, -75),(-125, -80),(0, -85),(125, -80),(200, -75)],
    [(-175, -135),(-105, -140),(0, -145),(105, -140),(175, -135)],
    [(-140, -185),(-75, -190),(0, -195),(75, -190),(140, -185)],
    [(-90, -220),(-45, -225),(0, -230),(45, -225),(90, -220)]
]

window = turtle.Screen()

turtle.speed(2)

# window.tracer(0) 

turtle.hideturtle()

turtle.bgcolor("#040720")

def draw_head(head_face_list):
    turtle.penup()
    turtle.goto(head_face_list[0])
    turtle.pendown()    
    turtle.color("#800000", "#C70039") 
    turtle.begin_fill()
    for x, y in head_face_list:
        turtle.goto(x, y)
    turtle.end_fill()  

def draw_eye(eye_list):
    turtle.penup()
    turtle.goto(eye_list[0])
    turtle.pendown()    
    turtle.color("#FFFFFF", "#FFFFFF")
    turtle.begin_fill()
    for x, y in eye_list:
        turtle.goto(x, y)
    turtle.end_fill() 

def draw_web_lines(lines_list):
    turtle.color("#FFFFFF")
    turtle.pensize(2)
    for line in lines_list:
        turtle.penup()
        turtle.goto(line[0])
        turtle.pendown()
        turtle.goto(line[1])

def draw_web_rings(rings_list):
    turtle.color("#FFFFFF")
    turtle.pensize(1)
    for ring in rings_list:
        turtle.penup()
        turtle.goto(ring[0])
        turtle.pendown()
        for x, y in ring:
            turtle.goto(x, y)


draw_head(head)        
draw_eye(left_eye)
draw_eye(right_eye)
draw_web_lines(web_lines)
draw_web_rings(web_rings)

window.update() 
turtle.mainloop()