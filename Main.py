from tkinter import *
from Ball import *
from Bat import *
import time

win = Tk()

win.title("PingPong Game")

# Creating a canvas to draw on.
canvas = Canvas(win, width = 500, height =  400, bg = "white")
canvas.pack()

# Creating a score counter which increments when u sucessfully hit the bal.
label = canvas.create_text(5, 5, anchor=NW, text="Score: 0")
win.update()

# Creating the Ball and Bat.
b2 = Bat(canvas, 'blue') #bat
b1 = Ball(canvas, 'red', 25, b2) #ball

highscore = 0

# Running the game until the ball hit the bottom
while b1.hit_bottom == False:
    b1.draw()
    b2.draw()
    canvas.itemconfig(label, text="Score: "+str(b1.score))
    highscore = max(highscore, b1.score)
    win.update_idletasks()
    win.update()
    time.sleep(0.01)

# When the Ball hit the bottom then Game Over
go_label = canvas.create_text(250,200,text="GAME OVER",font=("Helvetica",30))
win.update()

win.mainloop()
