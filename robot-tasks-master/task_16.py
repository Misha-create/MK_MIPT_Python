#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_22():
    x = False
    if wall_is_on_the_left() == wall_is_on_the_right():
        x = True
    print(x)
    if x == False:
        if wall_is_on_the_left() == False:
            while wall_is_on_the_left() == False:
                move_left(1)
        else:
            while wall_is_on_the_right() == False:
                move_right(1)
        if wall_is_beneath() == False:
            while wall_is_beneath() == False:
                move_down(1)
        else:
            while wall_is_above() == False:
                move_up(1)
    if x == True:
        if wall_is_above() == False:
            while wall_is_above() == False:
                move_up(1)
        else:
            while wall_is_beneath() == False:
                move_down(1)
        if wall_is_on_the_left() == False:
            while wall_is_on_the_left() == False:
                move_left(1)
        else:
            while wall_is_on_the_right() == False:
                move_right(1)
                
          
if __name__ == '__main__':
    run_tasks()
