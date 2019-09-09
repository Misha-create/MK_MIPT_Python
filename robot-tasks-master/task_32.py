#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_18():
    is_it_end = False
    v = 0
    x =0
    while not is_it_end:
        while wall_is_above():
            fill_cell()
            move_right(1)
        while not wall_is_above():
            move_up(1)
            if cell_is_filled():
                v+=1
            else:
                fill_cell()
        while not wall_is_beneath():
            move_down(1)
        t=0
        move_right(1)
        while wall_is_above() == True:
            move_right(1)
            t+=1
        if wall_is_on_the_right():
            is_it_end = True
            x=t
        move_left(t+1)
        move_right(1)
    for i in range(t):
        fill_cell()
        move_right(1)
    mov('ax',v)
if __name__ == '__main__':
    run_tasks()
