#!/usr/bin/python3

from pyrob.api import *


@task
def task_3_3():
    if wall_is_above() == wall_is_beneath():
        if wall_is_on_the_left() == True:
            move_right(1)
        else:
            move_left(1)
    else:
        if wall_is_above() == True:
            move_down(1)
        else:
            move_up(1)      
         
if __name__ == '__main__':
    run_tasks()
