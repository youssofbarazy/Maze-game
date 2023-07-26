import random
import turtle
import math

#Setting up the Maze
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Bit Maze Game")
wn.setup(700, 700)
wn.tracer(0)

#Set up class for each element (Maze, Player, key, Treasure, heart, Enemy)
#Updated from V1
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
#Setup the death of Player by Enemy
    def is_collision(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 5:
            return True
        else:
            return False

class key(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("triangle")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.key = 1
        self.goto(x, y)
#Setup when Player collect the key
    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()

class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("classic")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)
#Setup when Player collect the Treasure
    def destroy(self):
        self.goto(2010, 2010)
        self.hideturtle()

class heart (turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.health = 1
        self.goto(x, y)
#Setup when Player collect the heart to increase Player's health
    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()
        
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
        self.direction = random.choice(["up", "down","left","right"])
#Setup Automaticaaly moves of Enemy based on the distance
    def move(self):
        if self.direction == "up":
            dx = 0
            dy = 24
        elif self.direction == "down":
            dx = 0
            dy = -24
        elif self.direction == "left":
            dx = -24
            dy = 0
            self.shape("turtle")           
        elif self.direction == "right":
            dx = 24
            dy = 0
            self.shape("turtle")
        else:
            dx = 0
            dy = 0

        if self.is_close(player):
            if player.xcor() < self.xcor():
                self.direction = "left"
            if player.xcor() > self.xcor():
                self.direction = "right"
            if player.ycor() < self.ycor():
                self.direction = "down"
            if player.ycor() > self.ycor():
                self.direction = "up"

        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:

            self.direction = random.choice(["up", "down","left","right"])

        turtle.ontimer(self.move, t=random.randint(100,300))
#Decide the distance between Player & Distance
    def is_close(self,other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt ((a**2)+(b**2))
        if distance < 75:
            return True
        else:
            return False
        
levels = [""]

#24x24 Maze
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
"xxxxxxxxxxxxxxx      xxxx",
"xxxxxxxxxxxxxx        xxx",
"x        xxxxx xx K xxxxx",
"x  xxx   xxx   xx   xxxxx",
"x  xxx   xx  xxxxxxxxxxxx",
"x xxxx                Exx",
"x xxxx   xxxxxxxxxx    xx",
"x xxxx   xxxxxxxxxx    xx",
"x xxxxxxxxxx Txxxx    xxx",
"x          x xxxx      xx",
"x            xxxxx H  xxx",
"xxxxx   xxxxxxxxxxxxxxxxx",
"xxxxx   xxxxxxxxxxxxxxxxx",
"xxK        Exxxxxxxxxxxxx",
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
"xp xxxxxxx   x    x    Kx",
"x   xxxxx          xxx xx",
"xx        xxxxxx   Exx  x",
"xxxxxxxxxxxxxxx      x  x",
"xxxxxxxxxxxxxx          x",
"xx       xxxx  xxxxxxxxxx",
"xH  xx   xxx   xxxxxxxxxx",
"xXxxxx   xx  xxxxx   xxxx",
"xxxxxx                 xx",
"xxx      xxxxxxxxxx    xx",
"x   xx   xxxxxxxxxx    xx",
"xx xxxxxxxxxxxxxxx    xxx",
"x  xxxE    xxxxxx      xx",
"x             xxxx H  xxx",
"xxxxx   xxxx  xxxxxxxxxxx",
"xxxxx   xxxx  xxxxxxxxxxx",
"xx            xxxxxxxxxxx",
"xx          xxxxxxxxxxxxx",     
"xx xx xxxx   xxxxxxxxxxxx",
"xx K  xxxx   xxxxxxxxxxxx",
"xxxxxxxxx   xxxxxxxxxxxxx", 
"xT           E    xxxxxxx",
"x   E            Txxxxxxx",
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

turtle.listen()
turtle.onkey(player.go_left,"Left")
turtle.onkey(player.go_right,"Right")
turtle.onkey(player.go_up,"Up")
turtle.onkey(player.go_down,"Down")

wn.tracer(0)

for enemy in enemies:
    turtle.ontimer(enemy.move, t=250)


#main game loop
while True:
    for k in keys:
        if player.is_collision(k):
            player.key += k.key
            print ("Player Key: {}".format(player.key))
            k.destroy()
            keys.remove(k)

    for treasure in treasures:
        if player.is_collision(treasure):
            player.gold += treasure.gold
            print ("Player Gold: {}".format(player.gold))
            treasure.destroy()
            treasures.remove(treasure)

    for h in hearts:
        if player.is_collision(h):
            player.health += h.health
            print ("Player Health: {}".format(player.health))
            h.destroy()
            hearts.remove(h)
    
    for enemy in enemies:
        if player.gold > 0 and player.is_collision(enemy):
            player.gold -= enemy.gold
            print ("Player Robbed and Lost: {}".format (enemy.gold))

        elif player.health > 0 and player.is_collision(enemy):
            player.health -= enemy.damage
            print ("Player Lost: {} Health".format (enemy.damage))
#If Player Die, it will be sent back to the start point and reset the health to 3
        elif player.is_collision(enemy):
            print ("Player Died")
            player.penup()
            player.health = 3
            player.goto(-264, 264)

    wn.update()
#If the Player find the key & Tresure, cease the game
    if (len(keys) + len(treasures)) == 0:
        break

#Show up Wining Screen
wn = turtle.Screen()
wn.bgcolor("white")
turtle.write("You Won!", False, "center", font=('Arial', 96, 'bold'))
turtle.done()