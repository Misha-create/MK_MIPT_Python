#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():
    is_it_end = False
    while is_it_end == False:
        while wall_is_beneath() == False:
            move_down(1)
        while wall_is_on_the_right() == False and wall_is_beneath():
            move_right(1)
        if wall_is_beneath():
            while wall_is_on_the_left() == False and wall_is_beneath():
                move_left(1)
            if wall_is_beneath():
                is_it_end = True
            
    while wall_is_on_the_left() == False:
        move_left(1)

if __name__ == '__main__':
    run_tasks()
