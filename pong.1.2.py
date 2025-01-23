import turtle
import time

# Global variables
running = True
paused = False 


# create screen
screen = turtle.Screen()
screen.title("Pong Game")
screen.bgcolor("darkslategray") #used a different Color here
screen.setup(width=1000, height=600)


# Left paddle
leftPaddle = turtle.Turtle()
leftPaddle.speed(0)
leftPaddle.shape("square")
leftPaddle.color("white")
leftPaddle.shapesize(stretch_wid=5, stretch_len=1)
leftPaddle.penup()
leftPaddle.goto(-400, 0)


# Right paddle
rightPaddle = turtle.Turtle()
rightPaddle.speed(0)
rightPaddle.shape("square")
rightPaddle.color("white")
rightPaddle.shapesize(stretch_wid=5, stretch_len=1)
rightPaddle.penup()
rightPaddle.goto(400, 0)


# Ball of the circle variation
hitBall = turtle.Turtle()
hitBall.speed(40)
hitBall.shape("circle")
hitBall.color("cyan")
hitBall.penup()
hitBall.goto(0, 0)
hitBall.dx = 5 
hitBall.dy = -5


# Intialize the score
leftPlayer = 0
rightPlayer = 0

# Display the score
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("mistyrose")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write("Left Player: 0  --  Right Player: 0",
              align="center", font=("Courier", 24, "normal"))


# Functions to move paddles

def leftPaddleUp():
    y = leftPaddle.ycor()
    if y < 250: # Limit paddle movement
        y += 20
        leftPaddle.sety(y)


def leftPaddleDown():
    y = leftPaddle.ycor()
    if y > -240: # Limit paddle movement
        y -= 20
        leftPaddle.sety(y)


def rightPaddleUp():
    y = rightPaddle.ycor()
    if y < 250: # Limit paddle movement
        y += 20
        rightPaddle.sety(y)


def rightPaddleDown():
    y = rightPaddle.ycor()
    if y > -240: # Limit paddle movement
        y -= 20
        rightPaddle.sety(y)

# Pause and resume game
def pauseGame():
    global paused
    if not paused:
        paused = True
        # Create pause message in center
        pause_message = turtle.Turtle()
        pause_message.speed(0)
        pause_message.color("white")
        pause_message.penup()
        pause_message.hideturtle()
        pause_message.goto(0, 0)
        pause_message.write("GAME PAUSED\nL to resume\nM to Quit", 
                        align="center", font=("Courier", 36, "normal"))
        # Keep score visible
        sketch.clear()
        sketch.write(f"Left Player: {leftPlayer}  --  Right Player: {rightPlayer}",
                    align="center", font=("Courier", 24, "normal"))


def resumeGame():
    global paused
    if paused:
        paused = False
        # Clear all messages
        for turtle_obj in screen.turtles():
            if turtle_obj not in [leftPaddle, rightPaddle, hitBall, sketch]:
                turtle_obj.clear()
                turtle_obj.hideturtle()
        # Restore score display
        sketch.clear()
        sketch.write(f"Left Player: {leftPlayer}  --  Right Player: {rightPlayer}",
                    align="center", font=("Courier", 24, "normal"))


def closeGame():
    if paused:
        sketch.clear()
        sketch.write("Closing Game...", align="center", font=("Courier", 24, "normal"))
        time.sleep(2)
        global running
        running = False
        screen.bye()


# Keyboard bindings
screen.listen()
screen.onkeypress(leftPaddleUp, "w")
screen.onkeypress(leftPaddleDown, "s")
screen.onkeypress(rightPaddleUp, "Up")
screen.onkeypress(rightPaddleDown, "Down")
screen.onkeypress(pauseGame, "p")
screen.onkeypress(resumeGame, "l")
screen.onkeypress(closeGame, "m")


# Main game loop
while running:
    screen.update()
    
    if not paused:
        
        time.sleep(0.01)

        # Checking borders

        if hitBall.ycor() > 280:
            hitBall.sety(280)
            hitBall.dy *= -1

        if hitBall.ycor() < -280:
            hitBall.sety(-280)
            hitBall.dy *= -1

        if hitBall.xcor() > 500:
            hitBall.goto(0, 0)
            hitBall.dy *= -1
            leftPlayer += 1
            sketch.clear()
            sketch.write("Left Player: {}  --  Right Player: {}"
                        .format(leftPlayer, rightPlayer), 
                        align="center", font= ("Courier", 24, "normal"))
            
        if hitBall.xcor() < -500:
            hitBall.goto(0, 0)
            hitBall.dy *= -1
            rightPlayer += 1
            sketch.clear()
            sketch.write("Left Player: {}  --  Right Player: {}"
                        .format(leftPlayer, rightPlayer),
                        align="center", font= ("Courier", 24, "normal"))


        hitBall.setx(hitBall.xcor() + hitBall.dx)
        hitBall.sety(hitBall.ycor() + hitBall.dy)
    
        # Paddle and Ball collisions

        if (hitBall.xcor() > 360 and hitBall.xcor() < 370) and \
            (hitBall.ycor() < rightPaddle.ycor() + 50 and \
                hitBall.ycor() > rightPaddle.ycor() - 50):
            hitBall.setx(360)
            # Calculate relative impact point
            relativeImpact = (hitBall.ycor() - rightPaddle.ycor()) / 50
            # Adjust ball direction based on impact point
            hitBall.dx = -abs(hitBall.dx)
            hitBall.dy = 7 * relativeImpact

        if (hitBall.xcor() < -360 and hitBall.xcor() > -370) and \
            (hitBall.ycor() < leftPaddle.ycor() + 50 and \
                hitBall.ycor() > leftPaddle.ycor() - 50):
            # Calculate relative impact point
            relativeImpact = (hitBall.ycor() - leftPaddle.ycor()) / 50
            # Adjust ball direction based on impact point
            hitBall.dx = abs(hitBall.dx)
            hitBall.dy = 7 * relativeImpact

        # Game win state
        if leftPlayer == 5:
            sketch.clear()
            sketch.write("Left Player Wins!",
                        align="center", font= ("Courier", 24, "normal"))
            winMessage = turtle.Turtle()
            winMessage.speed(0)
            winMessage.color("white")
            winMessage.penup()
            winMessage.hideturtle()
            winMessage.goto(0, 0)
            winMessage.write("Closing Game...", 
                        align="center", font=("Courier", 36, "normal"))
            time.sleep(5)
            break

        if rightPlayer == 5:
            sketch.clear()
            sketch.write("Right Player Wins!")
            winMessage = turtle.Turtle()
            winMessage.speed(0)
            winMessage.color("white")
            winMessage.penup()
            winMessage.hideturtle()
            winMessage.goto(0, 0)
            winMessage.write("Closing Game...", 
                        align="center", font=("Courier", 36, "normal"))
            time.sleep(2)
            break
