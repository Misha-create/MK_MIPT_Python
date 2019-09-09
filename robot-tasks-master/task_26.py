#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_2_4():
    def move():
        move_right(1)
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
    move()
    for i in range(9):
        move_right(4)
        move()
    move_left(36)
    for i in range(4):
        move_down(4)
        move()
        for i in range(9):
            move_right(4)
            move()
        move_left(36)
    


if __name__ == '__main__':
    run_tasks()
