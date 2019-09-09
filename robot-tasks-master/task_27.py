#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    move_right(1)
    fill_cell()
    move_right(1)
    fill_cell()
    steps = 0
    y = 2
    while wall_is_on_the_right() == False:
        if y == steps:
            fill_cell()
            steps =0
            y+=1
        else:
            steps+=1
            move_right()
if __name__ == '__main__':
    run_tasks()
