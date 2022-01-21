from turtle import *
def triangle() :
	for count in range(3):
		forward(cote)
		left(120)
#reset()
speed(5)
#setposition(-140, 80)
right(90)
for count2 in range(6):
	forward(160)
	left(60)
cote = 160
for count3 in range(6):
	triangle()
	forward(160)
	left(60)
cote = 80
for count4 in range(6):
	forward(40)
	triangle()
	forward(120)
	left(60)
