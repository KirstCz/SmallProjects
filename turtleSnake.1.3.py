# Turtles 
# a Snake like Game
# modded by: KirstCz

import turtle
import time
import random

# Global variables
gamePaused = False
running = True

delay = 0.1

# Score starting point
score = 0
highScore = 0

# Set up the screen
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("wheat3")
screen.setup(width=1080, height=720)
screen.tracer(0) 

# Pause Screen
pauseMessage = turtle.Turtle()
pauseMessage.speed(0)
pauseMessage.color("black")
pauseMessage.penup()
pauseMessage.hideturtle()
pauseMessage.goto(0, 0)


# Lead Turtle 
lead = turtle.Turtle()
lead.speed(0)
lead.shape("turtle")
lead.shapesize(stretch_wid=2, stretch_len=2)
lead.color("SeaGreen") 
lead.penup()
lead.goto(0, 0)
lead.direction = "stop"

# Baby Turtle Egg
egg = turtle.Turtle()
egg.speed(0)
egg.shape("circle")
egg.shapesize(stretch_wid=1.5, stretch_len=1)
egg.color("seashell")
egg.penup()
egg.goto(0, 100)

segments = []

# Pen 
pen = turtle.Turtle()
pen.speed(0)
pen.shape("circle")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0",\
           align="center", font=("Futura", 24, "normal"))

# Functions
def goUp():
    if lead.direction != "down":
        lead.direction = "up"

def goDown():
        if lead.direction != "up":
            lead.direction = "down"

def goLeft():
        if lead.direction != "right":
            lead.direction = "left"

def goRight():
        if lead.direction != "left":
            lead.direction = "right"

def move():
    if lead.direction == "up":
        y = lead.ycor()
        lead.setheading(90)
        lead.sety(y + 20)

    if lead.direction == "down":
        y = lead.ycor()
        lead.setheading(270)
        lead.sety(y - 20)

    if lead.direction == "left":
        x = lead.xcor()
        lead.setheading(180)
        lead.setx(x - 20)

    if lead.direction == "right":
        x = lead.xcor()
        lead.setheading(0)
        lead.setx(x + 20)

def togglePause():
    global gamePaused
    if not gamePaused:
        gamePaused = True
        pauseMessage.clear()
        pauseMessage.penup()
        pauseMessage.goto(0, 0)
        pauseMessage.write("GAME PAUSED\n  P to RESUME\n  ESC to QUIT",\
                            align="center", font=("Futura", 36, "normal"))
    
    else:
        gamePaused = False
        pauseMessage.clear()

def quitGame():
    if gamePaused:
        global running
        running = False
        screen.bye()


# Keyboard bindings
screen.listen()
screen.onkeypress(goUp, "w")
screen.onkeypress(goDown, "s")
screen.onkeypress(goLeft, "a")
screen.onkeypress(goRight, "d")
screen.onkeypress(togglePause, "p")
screen.onkeypress(quitGame, "Escape")

# Main game loop

while running:
    screen.update()

    if gamePaused:
        screen.update()
        continue


    # Check for walls to loop to other side of screen
    if lead.xcor() > 530:
        lead.setx(-530)
    if lead.xcor() < -530:
        lead.setx(530)
    if lead.ycor() > 350:
        lead.sety(-350)
    if lead.ycor() < -350:
        lead.sety(350)
    
        
    # Check for a collision with the baby turtle egg
    if lead.distance(egg) < 20:
            # Move the egg to a random spot
        x = random.randint(-530, 530)
        y = random.randint(-350, 350)
        egg.goto(x, y)

        # Add a segment
        newSegment = turtle.Turtle()
        newSegment.speed(0)
        newSegment.shape("turtle")
        newSegment.color("SeaGreen3")
        newSegment.penup()
        segments.append(newSegment)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 1

        if score > highScore:
            highScore = score

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, highScore),\
                align="center", font=("Futura", 24, "normal"))
        
    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].setheading(segments[index-1].heading()) # babies turn
        segments[index].goto(x, y)

    # Move segment 0 to where the lead is
    if len(segments) > 0:
        x = lead.xcor()
        y = lead.ycor()
        segments[0].setheading(lead.heading()) # babies turn
        segments[0].goto(x, y)

    move()

    # Check for lead collision with the baby segments
    for segment in segments:
        if segment.distance(lead) < 20:
            time.sleep(1)
            lead.goto(0, 0)
            lead.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1

            # Update the score display
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, highScore),\
                        align="center", font=("Futura", 24, "normal"))
            
    time.sleep(delay)

screen.mainloop()    
