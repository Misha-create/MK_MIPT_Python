#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
    x =0
    y = True
    while wall_is_on_the_right()==False and y:
        move_right(1)
        if cell_is_filled():
            while cell_is_filled() and x<3:
                x+=1
                move_right(1)
        if x == 3:
            move_left(1)
            y = False
        else:
            x =0

if __name__ == '__main__':
    run_tasks()
