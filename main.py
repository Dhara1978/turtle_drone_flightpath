#Plot Flight Path of Drone Assignment
#import modules
import os
import turtle as t
from turtle import Screen

#declare functions to be used in main
def check_route(xcoord, ycoord):
  if xcoord > 600:
    print('Error: The route is outside of the grid')
  if ycoord > 600:
    print('Error: The route is outside of the grid')
  if xcoord < -600:
    print('Error: The route is outside of the grid')
  if ycoord < -600:
    print('Error: The route is outside of the grid')

def route_plotter(route, drone_colour):
  
  screen = Screen()
  drone = t.Turtle()
  t.pencolor(drone_colour)

  #set up screen, centre of the screen is 0,0 (bottom left is -600, -600)
  screen.setup (width=1220, height=1220, startx=0, starty=0)
  screen.bgcolor('#B7E3F1')

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
      print('X:' + str(int(actualxcoord)) + ', Y:' + str(int(actualycoord)))
      check_route(startxcoord, startycoord)
    elif i == 'E':
      startxcoord += 100
      t.goto(startxcoord, startycoord)
      actualxcoord = (startxcoord + 600)/100
      actualycoord = (startycoord + 600)/100
      print('X:' + str(int(actualxcoord)) + ', Y:' + str(int(actualycoord)))
      check_route(startxcoord, startycoord)
    elif i == 'S':
      startycoord -= 100
      t.goto(startxcoord, startycoord)
      actualxcoord = (startxcoord + 600)/100
      actualycoord = (startycoord + 600)/100
      print('X:' + str(int(actualxcoord)) + ', Y:' + str(int(actualycoord)))
      check_route(startxcoord, startycoord)
    elif i == 'W':
      startxcoord -= 100
      t.goto(startxcoord, startycoord)
      actualxcoord = (startxcoord + 600)/100
      actualycoord = (startycoord + 600)/100
      print('X:' + str(int(actualxcoord)) + ', Y:' + str(int(actualycoord)))
      check_route(startxcoord, startycoord)

def main():

  i = 0

  for file in os.listdir():
    ext = os.path.splitext(file)[-1].lower()

    if ext == '.txt':
      with open(file) as f:
        nf = f.read().splitlines()    
        drone_colors = ['red', 'green', 'blue']
        drone_color = drone_colors[i]
        i += 1
        route_plotter(nf, drone_color)
    else:
      print('It\'s not a text document')
  
  print('')


if __name__ == '__main__':
  main()
