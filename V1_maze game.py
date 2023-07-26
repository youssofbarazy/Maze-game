import random
import turtle

#Setting up the Maze
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Bit Maze Game")
wn.setup(700, 700)
wn.tracer(0)

#Set up class for each element (Maze, Player, key, Treasure, heart, Enemy)
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
        self.shape('square')
        self.color("green")
        self.penup()
        self.speed(0)
        self.key = 0
        self.gold = 0
        self.health = 3
#Direction setup for player
    def go_up(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor() + 24
        
        self.seth(90)
        self.shape()
        
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_down(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor() - 24

        self.seth(270)
        self.shape()

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        
    def go_left(self):
        move_to_x = self.xcor() - 24
        move_to_y = self.ycor()

        self.seth(180)
        self.shape()

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_right(self):
        move_to_x = self.xcor() + 24
        move_to_y = self.ycor()

        self.seth(0)
        self.shape()

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

class key(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("triangle")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.key = 1
        self.goto(x, y)

class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("classic")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)

class heart (turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.health = 1
        self.goto(x, y)
        
class Enemy(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("turtle")
        self.color("red")
        self.penup()
        self.speed(0)
        self.gold = 25
        self.damage = 1
        self.goto(x, y)
    
levels = [""]

#Maze Sample Structure
level_1 = [
"xxxxxxxxxxxxxxxxxxxxxxxxx",
"xp xxxxxxx        Exxxxxx",
"x   xxxxx          xxxxxx",
"xx          xxxx   xxxxxx",
"xx  xxxxxxxxxxx      xxxx",
"xx  xxxxxxxxxx        xxx",
"xxH      xxxxxx   K  xxxx",
"xxxxxx   xxxxxxx    xxxxx",
"xxxxxx   xxxxxxxxxxxxxxxx",
"xxxxxx                 xx",
"xxxxxx   xxxxxxxxxx    xx",
"xxxxxx   xxxxxxxxxx    xx",
"xxxxxx   xxxxxxxxx    xxx",
"x          xxxxxx      xx",
"x E          xxxxx    xxx",
"xxxxx   xxxxxxxxxxxxxxxxx",
"xxxxx   xxxxxxxxxxxxxxxxx",
"xx          xxxxxxxxxxxxx",
"xx          xxxxxxxxxxxxx",     
"xxxxxxxxx   xxxxxxxxxxxxx",
"xxxxxxxxx   xxxxxxxxxxxxx",
"xxxxxxxxx   xxxxxxxxxxxxx", 
"xE                xxxxxxx",
"x                Txxxxxxx",
"xxxxxxxxxxxxxxxxxxxxxxxxx"
]

level_2 = [
"xxxxxxxxxxxxxxxxxxxxxxxxx",
"xp xxxxxxx        Exxxxxx",
"x   xxxxx          xxxxxx",
"xx          xxxx   xxxxxx",
"xx  xxxxxxxxxxx      xxxx",
"xx  xxxxxxxxxx        xxx",
"xxH      xxxxxx   K  xxxx",
"xxxxxx   xxxxxxx    xxxxx",
"xxxxxx   xxxxxxxxxxxxxxxx",
"xxxxxx                 xx",
"xxxxxx   xxxxxxxxxx    xx",
"xxxxxx   xxxxxxxxxx    xx",
"xxxxxx   xxxxxxxxx    xxx",
"x          xxxxxx      xx",
"x E          xxxxx    xxx",
"xxxxx   xxxxxxxxxxxxxxxxx",
"xxxxx   xxxxxxxxxxxxxxxxx",
"xx          xxxxxxxxxxxxx",
"xx          xxxxxxxxxxxxx",     
"xxxxxxxxx   xxxxxxxxxxxxx",
"xxxxxxxxx   xxxxxxxxxxxxx",
"xxxxxxxxx   xxxxxxxxxxxxx", 
"xE                xxxxxxx",
"x                Txxxxxxx",
"xxxxxxxxxxxxxxxxxxxxxxxxx"
]

level_3 = [
"xxxxxxxxxxxxxxxxxxxxxxxxx",
"xp xxxxxxxx       Exxxxxx",
"x   xxxxx          xxxxxx",
"xx          xxxx   xxxxxx",
"xx  xxxxxxxxxxx      xxxx",
"xx  xxxxxxxxxx        xxx",
"xxH      xxxxxx   K  xxxx",
"xxxxxx   xxxxxxx    xxxxx",
"xxxxxx   xxxxxxxxxxxxxxxx",
"xxxxxx                 xx",
"xxxxxx   xxxxxxxxxx    xx",
"xxxxxx   xxxxxxxxxx    xx",
"xxxxxx   xxxxxxxxx    xxx",
"x          xxxxxx      xx",
"x E          xxxxx    xxx",
"xxxxx   xxxxxxxxxxxxxxxxx",
"xxxxx   xxxxxxxxxxxxxxxxx",
"xx          xxxxxxxxxxxxx",
"xx          xxxxxxxxxxxxx",     
"xxxxxxxxx   xxxxxxxxxxxxx",
"xxxxxxxxx   xxxxxxxxxxxxx",
"xxxxxxxxx   xxxxxxxxxxxxx", 
"xE                xxxxxxx",
"x                Txxxxxxx",
"xxxxxxxxxxxxxxxxxxxxxxxxx"
]

#Choose random maze structure from 3 levels and add it to maze list
level_set = [level_1, level_2, level_3]
levels.append(level_set[random.randint(0, len(level_set)-1)])

pen = Pen()
player = Player()

#Set up the numbers of keys, treasures, enemies and hearts
keys = []#K
treasures = []#T
enemies = []#E
hearts = [] #H

#Create the walls
walls = []

#Create Level Setup Function
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            if character == "x":
                pen.goto(screen_x, screen_y)
                pen.shape("square")
                pen.stamp()
                
                walls.append((screen_x, screen_y))
                
            if character == "p":
                player.goto(screen_x, screen_y)

            if character == "K":
                keys.append(key(screen_x, screen_y))

            if character == "T":
                treasures.append(Treasure(screen_x, screen_y))

            if character == "E":
                enemies.append(Enemy(screen_x, screen_y))

            if character == "H":
                hearts.append(heart(screen_x, screen_y))

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