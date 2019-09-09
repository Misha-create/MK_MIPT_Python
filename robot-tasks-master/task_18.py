#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_28():
    x = False
    if wall_is_above() == False:
        x=True
    print(x)
    if wall_is_on_the_left() == False:
        while wall_is_on_the_left() == False and x == False:
            move_left(1)        
            if wall_is_above() == False:
                x=True
    if wall_is_on_the_right() == False:
        while wall_is_on_the_right() == False and x == False:
            move_right(1)        
            if wall_is_above() == False:
                x=True
    while wall_is_above() == False:
        move_up(1)
    while wall_is_on_the_left() == False:
        move_left(1)
if __name__ == '__main__':
    run_tasks()
