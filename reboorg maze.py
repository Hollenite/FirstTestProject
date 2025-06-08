# DEBUG PENDING
def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    while wall_on_right():
        if front_is_clear():
            move()
        elif wall_in_front():
            turn_left()
    while right_is_clear():
        if wall_in_front():
            turn_right()
            move()
        elif front_is_clear():
            turn_right()
            move()










