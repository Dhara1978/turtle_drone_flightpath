"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""
#import modules
import turtle as t
from turtle import Screen

screen = Screen()
drone = t.Turtle()

#set up screen, centre of the screen is 0,0 (bottom left is -600, -600)
screen.setup (width=1220, height=1220, startx=0, starty=0)
screen.bgcolor('#B7E3F1')

#list of starting position and direction travelled
route = ['3', '12', 'S', 'S', 'W', 'S', 'S', 'S', 'E', 'E', 'E', 'S', 'S', 'W', 'W', 'S', 'E', 'E', 'E', 'E', 'N', 'N', 'N', 'N', 'W', 'N', 'N', 'E', 'E', 'S', 'E', 'S', 'E', 'S', 'S', 'W', 'S', 'S', 'S', 'S', 'S', 'E', 'N', 'E', 'E', 'E']

def check_route(xcoord, ycoord):
  if xcoord > 600:
    print('Error: The route is outside of the grid')
  if ycoord > 600:
    print('Error: The route is outside of the grid')

startxcoord = int(route[0]) * 100 - 600
startycoord = int(route[1]) * 100 - 600
print(startxcoord, startycoord)
print('X:' + route[0] + ', Y:' + route[1])
t.pensize(width = 8)

#starting position
t.penup()
t.goto(startxcoord, startycoord)
t.pendown()

#directions travelled
directions = route[2:]

for i in directions:
  if i == 'N':
    startycoord += 100
    t.goto(startxcoord, startycoord)
    actualxcoord = (startxcoord + 600)/100
    actualycoord = (startycoord + 600)/100
    print('X:' + str(actualxcoord) + ', Y:' + str(actualycoord))
    check_route(startxcoord, startycoord)
  elif i == 'E':
    startxcoord += 100
    t.goto(startxcoord, startycoord)
    actualxcoord = (startxcoord + 600)/100
    actualycoord = (startycoord + 600)/100
    print('X:' + str(actualxcoord) + ', Y:' + str(actualycoord))
    check_route(startxcoord, startycoord)
  elif i == 'S':
    startycoord -= 100
    t.goto(startxcoord, startycoord)
    actualxcoord = (startxcoord + 600)/100
    actualycoord = (startycoord + 600)/100
    print('X:' + str(actualxcoord) + ', Y:' + str(actualycoord))
    check_route(startxcoord, startycoord)
  elif i == 'W':
    startxcoord -= 100
    t.goto(startxcoord, startycoord)
    actualxcoord = (startxcoord + 600)/100
    actualycoord = (startycoord + 600)/100
    print('X:' + str(actualxcoord) + ', Y:' + str(actualycoord))
    check_route(startxcoord, startycoord)