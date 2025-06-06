# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# def turn_around():
#     turn_left()
#     turn_left()
#
#
# while not at_goal():
#     if front_is_clear():
#         move()
#     else:
#         turn_left()
#         if wall_in_front():
#             turn_left()
#             move()
#         else:
#             move()
#         while front_is_clear():
#             turn_right()
#             if wall_in_front():
#                 turn_left()
#                 move()
#             else:
#                 move()
#         if wall_in_front():
#             turn_right()
#             if wall_in_front():
#                 turn_around()
#                 if wall_in_front():
#                     turn_left()
#                     move()
#                 else:
#                     move()
#             else:
#                 move()
#         turn_right()
#         if wall_in_front():
#             turn_left()
#         while front_is_clear():
#             turn_right()
#             if wall_in_front():
#                 turn_left()
#                 move()
#             else:
#                 if front_is_clear():
#                     move()
#                     if front_is_clear():
#                         turn_around()
#                         move()
#                         turn_right()
#                         move()
#                     else:
#                         turn_around()
#                         move()
#                         turn_around()
#                 else:
#                     turn_left()
#                     move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def turn_around():
    turn_left()
    turn_left()


def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    move()
    while front_is_clear():
        move()
    turn_left()


while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()





