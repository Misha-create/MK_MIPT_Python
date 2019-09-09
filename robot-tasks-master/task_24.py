#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_1():
    move_right(2)
    move_down(1)
    fill_cell()
    for i in range(2):
        move_down(1)
        fill_cell()
    move_left(1)
    move_up(1)
    fill_cell()
    for i in range(2):
        move_right(1)
        fill_cell()
    move_left(2)
    move_up(1)
if __name__ == '__main__':
    run_tasks()
