#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_29():
    x = False
    while wall_is_on_the_left() == False:
        move_left(1)
    if wall_is_above() == False:
        x = True
    if x == False:
        while wall_is_on_the_right() == False:
            move_right(1)
        if wall_is_above() == False:
            x = True
    if x:
        while wall_is_above() == False:
            move_up(1)
        while wall_is_on_the_left() == False:
            move_left(1)
if __name__ == '__main__':
    run_tasks()
