import turtle

#Setting up the Maze
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Bit Maze Game")
wn.setup(700, 700)

#Set up class for Maze & Player
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
        
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)
    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 24)
    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 24)
    def go_left(self):
        self.goto(self.xcor()-24, self.ycor())
    def go_right(self):
        self.goto(self.xcor()+24, self.ycor())
    

levels = [""]

#Maze Sample Structure
level_1 = [
"xxxxxxxxxxxxxxxxxxxxxxxxx",
"xp xxxxxxx         xxxxxx",
"x   xxxxx          xxxxxx",
"xx          xxxx   xxxxxx",
"xx  xxxxxxxxxxx      xxxx",
"xx  xxxxxxxxxx        xxx",
"xx       xxxxxx      xxxx",
"xxxxxx   xxxxxxx    xxxxx",
"xxxxxx   xxxxxxxxxxxxxxxx",
"xxxxxx                 xx",
"xxxxxx   xxxxxxxxxx    xx",
"xxxxxx   xxxxxxxxxx    xx",
"xxxxxx   xxxxxxxxx    xxx",
"x          xxxxxx      xx",
"x            xxxxx    xxx",
"xxxxx   xxxxxxxxxxxxxxxxx",
"xxxxx   xxxxxxxxxxxxxxxxx",
"xx          xxxxxxxxxxxxx",
"xx          xxxxxxxxxxxxx",     
"xxxxxxxxx   xxxxxxxxxxxxx",
"xxxxxxxxx   xxxxxxxxxxxxx",
"xxxxxxxxx   xxxxxxxxxxxxx", 
"x                 xxxxxxx",
"x                 xxxxxxx",
"xxxxxxxxxxxxxxxxxxxxxxxxx"
]

#Add maze to maze list
levels.append(level_1)

pen = Pen()
player = Player()

#Create the walls
walls = [] 

#Create Level Setup Function
def setup_maze(level):
    num = len(level)
    for x in range(len(level)):
        for y in range(len(level)):
            character = level[x][y]
            screen_x = -288 + (x * num)
            screen_y = 288 - (y*num)
            
            if character == "x":
                pen.goto(screen_x, screen_y)
                pen.stamp()
            if character == "p":
                player.goto(screen_x, screen_y)

setup_maze(levels[1])

#Move the player
turtle.listen()
turtle.onkey(player.go_left, "Left")
turtle.onkey(player.go_right, "Right")
turtle.onkey(player.go_up, "Up")
turtle.onkey(player.go_down, "Down")

#Turnoff Screen Updates
wn.tracer(0)

#Main Game Loop
while True:
    wn.update()