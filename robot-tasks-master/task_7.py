#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_4():
    while wall_is_beneath()==False:
        move_down(1)
    while wall_is_beneath():
        move_right(1)
    move_down(1)
    while wall_is_on_the_left()==False:
        move_left(1)	
if __name__ == '__main__':
    run_tasks()
