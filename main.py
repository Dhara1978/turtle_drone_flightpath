#import packages
import os
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image
import turtle as t
from turtle import Screen

#gui functions
def help_func():
    messagebox.showinfo('Help', 'This GUI is to plot the path of a drone in a 12 x 12 square and raise a warning for the drone exiting the square')

#app functions
def check_route(xcoord, ycoord):
  if xcoord > 600:
    print('Error: The route is outside of the grid')
    messagebox.showinfo('Error:', 'The route is outside of the grid')
  if ycoord > 600:
    print('Error: The route is outside of the grid')
    messagebox.showinfo('Error:', 'The route is outside of the grid')
  if xcoord < -600:
    print('Error: The route is outside of the grid')
    messagebox.showinfo('Error:', 'The route is outside of the grid')
  if ycoord < -600:
    print('Error: The route is outside of the grid')
    messagebox.showinfo('Error:', 'The route is outside of the grid')

def route_plotter(route):

  screen = Screen()
  drone = t.Turtle()

  #set up screen, centre of the screen is 0,0 (bottom left is -600, -600)
  screen.setup (width=1.0, height=1.0, startx=0, starty=0)
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


def plot_route():

    file = filedialog.askopenfilename()
    ext = os.path.splitext(file)[-1].lower()

    try:
        if ext == '.txt':
            with open(file) as f:
                nf = f.read().splitlines()
                route_plotter(nf)
        else:
            messagebox.showinfo('Info', 'This is not a text file')
    except:
        print('this is an exception')


    print('')

#window setup
window = Tk()
window.title("Hello wold")
window.geometry("700x560")
#use image as background
bg_img = ImageTk.PhotoImage(Image.open('daz_project.gif'))
panel = Label(image = bg_img)
panel.place(x = 0, y = 0, relwidth = 1, relheight = 1)

hello = Label(text="Drone Flight Path GUI")
hello.pack()
button = Button(text="Help", fg = 'green', command = help_func)
button.place(x = 350, y = 220)
button = Button(text="Plot Route", fg = 'green', command = plot_route)
button.place(x = 335, y = 320)



window.mainloop()
