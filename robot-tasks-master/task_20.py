#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    move_right(1)
    for i in range(6):
        for r in range(25):
            fill_cell()
            move_right(1)
        fill_cell()
        move_right(1)
        fill_cell()
        move_down(1)
        for t in range(25):
            fill_cell()
            move_left(1)
        fill_cell()
        move_left(1)
        fill_cell()
        move_down(1)    

if __name__ == '__main__':
    run_tasks()
