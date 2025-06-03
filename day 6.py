#rebborgs world
#Hurdle 1
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def one_loop():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for step in range(0, 6):
    one_loop()
# one_loop()
# one_loop()
# one_loop()
# one_loop()
# one_loop()
# one_loop()