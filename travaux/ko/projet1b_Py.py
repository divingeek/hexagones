from turtle import * 
def triangle_equilateral():
	for count in range(3):
		forward(160)
		left(120)
speed(10)
#setposition((-140), 80)
right(90)
pendown()
for count2 in range(6):
	forward(160)
	left(60)
for count3 in range(6):
	triangle_equilateral()
	forward(160)
	left(60)
x = 1
for count5 in range(19):
	setposition((-140 + x * 7), (80 - x * 4))
	for count4 in range(6):
		forward((160 - x * 8))
		left(60)
	x = x + 1
