#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    move_right(1)
    move_down(1)
    fill_cell()
    move_down(1)
    for i in range(12):
        fill_cell()
        for t in range(i+1):
            move_right(1)
            fill_cell()
        move_left(i+1)
        move_down(1)
        


if __name__ == '__main__':
    run_tasks()
