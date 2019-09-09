#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_6_6():
    x = 0;
    move_right(1)
    while wall_is_on_the_right() == False:
        if wall_is_above() == False:
            while wall_is_above() == False:
                move_up(1)
                fill_cell()
            while wall_is_beneath() == False:
                move_down(1)
        if wall_is_beneath() == False:
            while wall_is_beneath() == False:
                move_down(1)
                fill_cell()
            while wall_is_above() == False:
                move_up(1)
        x = x+1
        move_right(1)
    if wall_is_above() == False:
        while wall_is_above() == False:
            move_up(1)
            fill_cell()
        while wall_is_beneath() == False:
            move_down(1)
    if wall_is_beneath() == False:
        while wall_is_beneath() == False:
            move_down(1)
            fill_cell()
        while wall_is_above() == False:
            move_up(1)
    move_left(x+1)
if __name__ == '__main__':
    run_tasks()
