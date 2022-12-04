
from tkinter import *

 
win = Tk()
win.title("Animation")

canvas_width = 800
canvas_height = 800  
canvas=Canvas(win, 
width=canvas_width, 
height=canvas_height)

rect1=canvas.create_rectangle((canvas_width/2)-100,(canvas_height/2)-100,canvas_width/2, canvas_height/2, fill='blue',outline="black", width=3)
rect2=canvas.create_rectangle((canvas_width/2)-100,canvas_height/2 ,canvas_width/2 ,(canvas_height/2)+100 , fill='yellow',outline="black", width=3 )
rect3=canvas.create_rectangle(canvas_width/2,(canvas_height/2)-100,(canvas_width/2)+100 ,canvas_height/2 ,fill='red',outline="black", width=3)
rect4=canvas.create_rectangle(canvas_width/2, canvas_height/2,(canvas_width/2)+100,(canvas_height/2)+100,  fill='green',outline="black", width=3)
canvas.pack()

def redraw(): 
    canvas.after(30,redraw)
    canvas.move(rect1,-7,-7)
    canvas.move(rect2,-7,7)
    canvas.move(rect3,7,-7)
    canvas.move(rect4,7,7)

redraw()
win.mainloop()
   
