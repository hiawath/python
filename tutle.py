import turtle
from tkinter.simpledialog import*
import random

chX,chX, chSize = [0],[0],[0]
sizeWidth, sizeHeight = 500, 500


turtle.title('거북이')
turtle.setup(width=sizeWidth+50, height=sizeHeight+50)
turtle.screensize(sizeWidth,sizeHeight)

turtle.penup()
turtle.shape('turtle')

inStr = askstring('문자열 입력', '거북이 쓸 문자열을 입력')

for ch in inStr:
    chX=random.randrange(-sizeWidth/2,sizeWidth/2)
    chY=random.randrange(-sizeWidth/2,sizeHeight/2)
    red=random.random()
    green=random.random()
    blue=random.random()
    chSize=random.randrange(50,100)
    
    turtle.goto(chX,chY)
    turtle.pencolor(red, green,blue)
    turtle.write(ch,move=False,align="center", font=("HYPost", chSize, "italic"))
    
    
turtle.done()