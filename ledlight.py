from sense_hat import SenseHat

sense=SenseHat()

def green():
        sense.clear(0,255,0)


def blue():
        sense.clear(0,0,139)


def black():
        sense.clear(0,0,0)


def red():
        sense.clear(165,42,42)


sense.stick.direction_up=red
sense.stick.direction_down=green
sense.stick.direction_right=blue
sense.stick.direction_left=black
sense.stick.direction_middle=sense.clear()

while True:
	pass
