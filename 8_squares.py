import turtle

turtle.pensize(7)
turtle.pencolor("pink")

# Declaratii
colors = ["pink","green","yellow","orange","red","blue","grey","black"]
CONTOR = 0
c = 0
Create = True
# Make squares

while Create:
    i = 0
    turtle.pencolor(colors[c])
    c += 1
    for i in range (0,4):
        turtle.forward(100)
        turtle.left(90)
        i += 1
    turtle.right(90)
    CONTOR += 1
    if CONTOR == 4:
        Create = False

turtle.right(45)
CONTOR = 0
Create = True

while Create:
    i = 0
    turtle.pencolor(colors[c])
    c += 1
    for i in range (0,4):
        turtle.forward(100)
        turtle.left(90)
        i += 1
    turtle.right(90)
    CONTOR += 1
    if CONTOR == 4:
        Create = False
