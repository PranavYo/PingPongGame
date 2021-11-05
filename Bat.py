# Creating a class for the Bat
class Bat:
    def __init__(self, canvas, color):
        self.canvas = canvas
        # Creating a bat
        self.id = canvas.create_rectangle(0,0, 100, 10, fill=color)
        self.canvas.move(self.id, 300, 300)
        self.xspeed = 0
        # When the left key is pressed the bat moves left
        self.canvas.bind_all('<KeyPress-Left>', self.move_left)
        # When the right key is pressed the bat moves right
        self.canvas.bind_all('<KeyPress-Right>', self.move_right)
        # When nothing is pressed the Bat stops moving
        self.canvas.bind_all('<KeyRelease>', self.stop)

    def draw(self):
        self.canvas.move(self.id, self.xspeed, 0)
        pos = self.canvas.coords(self.id)
        # Handling the border cases
        if pos[0] <= 0:
            self.xspeed = 0
        if pos[2] >= 500:
            self.xspeed = 0

    # Appropriate method is called when the key is pressed
    def move_left(self, evt):
       self.xspeed = -4
    def move_right(self, evt):
        self.xspeed = 4
    def stop(self, evt):
        self.xspeed = 0

