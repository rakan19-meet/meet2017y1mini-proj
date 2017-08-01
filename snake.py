import turtle
import random #We'll need this later in the lab
turtle.tracer(1,0) #This helps the turtle move more smoothly
SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y) 
turtle.penup()
SQUARE_SIZE = 20
START_LENGTH = 9
#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []
#Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.shape("square")
#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()

for i in range(START_LENGTH):
    x_pos=snake.pos()[0]
    y_pos=snake.pos()[1]
    x_pos+=SQUARE_SIZE

    my_pos=(x_pos,y_pos)
    snake.goto(x_pos,y_pos)
    pos_list.append(my_pos)

    stamp_list.append(snake.stamp())
    stamp_list.append(my_pos)

UP_ARROW="Up"
LEFT_ARROW="Left"
DOWN_ARROW="Down"
TIME_STEP=100
RIGHT_ARROW="Right"
SPACEBAR="space"


UP=0
DOWN=1
LEFT=2
RIGHT=3









direction = UP
def up():
    global direction#snake direction is global (same everywhere)
    direction=UP #Change direction to up
    move_snake() #Update the snake drawing <- remember me later
    print("You pressed the up key!")
#2. Make functions down(), left(), and right() that change direction
####WRITE YOUR CODE HERE!!

def down():
    global direction
    direction=DOWN
    move_snake()
    print("you pressed the down key")

def left():
    global direction
    direction=LEFT
    move_snake()
    print("you pressed the left key")

def right():
    global direction
    direction=RIGHT
    move_snake()
    print("you pressed the right key")
    
    
    
turtle.onkeypress(up, UP_ARROW) # Create listener for up key
#3. Do the same for the other arrow keys
####WRITE YOUR CODE HERE!!
turtle.listen()
def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    if direction==RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")
    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")
    elif direction==UP:
        snake.goto(y_pos+SQUARE_SIZE,x_pos)
        print("you moved up")
    elif direction==down:
        snake.goto(y_pos-SQUARE_SIZE,x-pos)
        print("you moved down")
    #4. Write the conditions for UP and DOWN on your own
    ##### YOUR CODE HERE
    #Stamp new element and append new stamp in list
    #Remember: The snake position changed - update my_pos()
    my_pos=snake.pos()
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)
    ######## SPECIAL PLACE - Remember it for Part 5
    #pop zeroth element in pos_list to get rid of last the last
    #piece of the tail
    old_stamp = stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    pos_list.pop(0)


          

turtle.onkeypress(down,DOWN_ARROW)
turtle.listen()

turtle.onkeypress(left,LEFT_ARROW)
turtle.listen()

turtle.onkeypress(right,RIGHT_ARROW)
turtle.listen()

