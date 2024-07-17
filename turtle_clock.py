import time
import datetime as dt
import turtle

# Create a turtle to display time
t = turtle.Turtle()

# Create a turtle to create a rectangle box
t1 = turtle.Turtle()

# Create screen
s = turtle.Screen()

# Set background color of the screen
s.bgcolor("green")

# Hide the turtle and set initial settings
t.hideturtle()
t.penup()
t.color("black")
t.goto(-60, -20)

# Set up the rectangle box turtle
t1.pensize(3)
t1.color('black')
t1.penup()
t1.goto(-100, -35)
t1.pendown()

# Create rectangular box
for i in range(2):
    t1.forward(200)
    t1.left(90)
    t1.forward(70)
    t1.left(90)

# Hide the rectangle box turtle
t1.hideturtle()

while True:
    # Clear the previous time
    t.clear()

    # Get the current time
    now = dt.datetime.now()
    hr = now.hour
    min = now.minute
    sec = now.second

    # Format and display the time
    t.write(f"{str(hr).zfill(2)}:{str(min).zfill(2)}:{str(sec).zfill(2)}",
            font=("Arial Narrow", 35, "bold"))

    # Wait for 1 second
    time.sleep(1)
