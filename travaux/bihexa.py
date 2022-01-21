def losange():
	for count4 in range(2):
		forward(80)
		left(120)
		forward(80)
		left(60)

speed(3)
setheading(180)
left(30)
pendown()
pencolor("blue")
# couleur stylo pas implémenté
for count in range(3):
	losange()
	left(120)
	pencolor(random.choice(couleurs))
	# couleur stylo pas implémenté
penup()
forward(80)
left(120)
forward(80)
right(60)
pendown()
forward(80)
left(120)
for count3 in range(3):
	for count2 in range(2):
		forward(160)
		left(60)
	left(60)
	forward(80)
	left(180)
	forward(80)
	left(120)
