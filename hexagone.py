#!/bin/python3

from turtle import *
from math import *
import time
import random
import os
WIDTH, HEIGHT = 1920, 1080

screen = Screen()
screen.setup(WIDTH + 4, HEIGHT + 8)  # fudge factors due to window borders & title bar
#screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
cote = 160

def listdir_nohidden(path):
	for f in os.listdir(path):
		if os.path.isfile(os.path.join(path, f)):
			if not f.startswith('.'):
				yield f

def carre(x,y,a):
	penup()
	setposition(x+a/2, y-a/2)
	left(30)
	pendown()
	for count in range(4):
		forward(a)
		left(90)

def hexagone(x,y,a):
	penup()
	setheading(90)
	xc=x+a*sqrt(3)/2
	yc=y-a/2
	#print(xc)
	#print(yc)

	setposition(xc, yc)
	pendown()
	for count in range(6):
		forward(a)
		left(60)

def travaux(x,y,a,n,name):
	penup()
	#setheading(90)
	xc=x+a*sqrt(3)/2
	yc=y-a/2
	setposition(xc, yc)
	pendown()
	#exec(open("./travaux/bihexa.py").read())
	exec(open("./travaux/"+name).read())
	penup()
	

couleurs = ["black","blue","green","red","brown","pink","grey","orange","purple","yellow"]

coordonnees = [(0,0),
(cote*sqrt(3),0),
(cote*sqrt(3)/2,3*cote/2),
(-cote*sqrt(3)/2,3*cote/2),
(-cote*sqrt(3),0),
(-cote*sqrt(3)/2,-3*cote/2),
(cote*sqrt(3)/2,-3*cote/2),
(2*cote*sqrt(3),0),
(-2*cote*sqrt(3),0)
]


path = "./travaux"

n = 6

def draw(cote):
	penup()
	speed(2)
	time.sleep(2)
	i = 0
	for j in range(n):
		print(str(j))
		files = listdir_nohidden(path)
		for f in files:
			print(f)
			#hexagone(coordonnees[i][0],coordonnees[i][1],cote)
			travaux(coordonnees[i][0],coordonnees[i][1],cote,i,f)
			i+=1
	#hexagone(cote*sqrt(3),0,cote)
	#hexagone(cote*sqrt(3)/2,3*cote/2,cote)
	#hexagone(-cote*sqrt(3)/2,3*cote/2,cote)
	time.sleep(2)
	ontimer(stop, 500)  # stop the recording (1/2 second trailer)

running = True
FRAMES_PER_SECOND = 10

def stop():
    global running
    running = False

def save(counter=[1]):
    getcanvas().postscript(file = "hgone{0:03d}.eps".format(counter[0]))
    counter[0] += 1
    if running:
        ontimer(save, int(1000 / FRAMES_PER_SECOND))

reset()
hideturtle()
save()  # start the recording

ontimer(draw(cote), 500)  # start the program (1/2 second leader)

exitonclick()
